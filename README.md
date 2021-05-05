# JWT Signing with Asymmetric AWS KMS key in Python

### Pre-Requisite

1. Make sure you are authenticated with AWS.
2. Make sure your AWS account has access to the KMS key used for Encryption.
3. Retrieve and Store Public Key locally from AWS KMS

### Usage

1. Install required packages,

```
pip3 install -r requirements.txt
```

2. Modify following vars in code,

```
aws_kms_key_arn = "KMS KEY ARN"
public_key_file_path = "public key pem file path"
```

