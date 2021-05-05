import base64
import datetime
import json
import time
import jwt


def _jwt_kms_assemtric_encryption(jwt_head, jwt_payload, aws_key_arn):
    jwt_payload["iat"] = round(time.time())
    jwt_payload["exp"] = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%s")

    token_components = {
        "header":  base64.urlsafe_b64encode(json.dumps(jwt_head).encode()).decode().rstrip("="),
        "payload": base64.urlsafe_b64encode(json.dumps(jwt_payload).encode()).decode().rstrip("="),
    }
    message = f'{token_components.get("header")}.{token_components.get("payload")}'
    client = _get_boto3_client("kms")
    response = client.sign(
        KeyId=aws_key_arn,
        Message=message.encode(),
        MessageType="RAW",
        SigningAlgorithm="RSASSA_PKCS1_V1_5_SHA_256"
    )
    token_components["signature"] = base64.urlsafe_b64encode(response["Signature"]).decode().rstrip("=")
    return f'{token_components.get("header")}.{token_components.get("payload")}.{token_components["signature"]}'
  
  
 if __name__ == "__main__":
    aws_kms_key_arn = "KMS KEY ARN"
    public_key_file_path = "public key pem file path"
    
    header = {
        "alg": "RS256",
        "typ": "JWT"
    }

    payload = {
        "user_name": "sufiyan-test"
    }
    
    jwt_encoded = _jwt_kms_assemtric_encryption(header, payload, aws_kms_key_arn)
    
    key = ""
    with open(public_key_file_path, "r") as f:
        key = f.read()
        
    # Decode JWT
    decoded_data = jwt.decode(jwt_encoded, key, algorithms=["RS256"])
    print(decoded_data)
