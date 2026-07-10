# 🚀 AWS Lambda - Automatic S3 File Copy

## 📌 Overview

This project demonstrates how to automatically copy files from one Amazon S3 bucket to another using AWS Lambda.

Whenever a new file is uploaded to the **Source S3 Bucket**, an **S3 Event Notification** triggers the Lambda function, which copies the uploaded file to the **Destination S3 Bucket**.

---

## 🏗️ Architecture

```
          Upload File
               │
               ▼
     Source S3 Bucket
               │
      S3 Event Trigger
               │
               ▼
        AWS Lambda Function
               │
               ▼
    Destination S3 Bucket
```

---

## 🛠️ AWS Services Used

- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon CloudWatch

---

## 📂 Resources Created

### Source Bucket

```
sumedh-source-bucket-12345
```

### Destination Bucket

```
sumedh-destination-bucket-12345
```

### Lambda Function

```
copy-s3-files
```

### IAM Role

```
copy-s3-files-role
```

### Environment Variable

| Key | Value |
|------|-------|
| destination_bucket | sumedh-destination-bucket-12345 |

---

## 🔐 IAM Policy

The Lambda execution role requires the following permissions:

- s3:GetObject
- s3:PutObject
- s3:ListBucket

---

## ⚙️ Workflow

1. Upload a file to the Source S3 Bucket.
2. S3 Event Notification triggers the Lambda function.
3. Lambda reads the uploaded object.
4. Lambda copies the object to the Destination S3 Bucket.
5. CloudWatch stores the execution logs.

---

## 📋 Lambda Code

```python
import boto3
import botocore
import os
import logging
from urllib.parse import unquote_plus

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.resource('s3')

def lambda_handler(event, context):

    logger.info("New files uploaded to the source bucket.")
    logger.info(event)

    try:

        source_bucket = event['Records'][0]['s3']['bucket']['name']
        key = unquote_plus(event['Records'][0]['s3']['object']['key'])
        destination_bucket = os.environ['destination_bucket']

        logger.info(f"Source Bucket: {source_bucket}")
        logger.info(f"Destination Bucket: {destination_bucket}")
        logger.info(f"Object Key: {key}")

        source = {
            'Bucket': source_bucket,
            'Key': key
        }

        s3.meta.client.copy(source, destination_bucket, key)

        logger.info("File copied successfully!")

        return {
            "statusCode": 200,
            "body": "File copied successfully."
        }

    except botocore.exceptions.ClientError as error:
        logger.error(f"AWS Client Error: {error}")
        raise error

    except Exception as error:
        logger.error(f"Unexpected Error: {error}")
        raise error
```

---

## 🧪 Testing

Upload any file to:

```
sumedh-source-bucket-12345
```

Example:

```
Screenshot (1278).png
```

---

## ✅ Expected Result

- Lambda is triggered automatically.
- File is copied to the destination bucket.
- CloudWatch logs show successful execution.

---

## 📸 Demo Result

✔ Source Bucket Created

✔ Destination Bucket Created

✔ IAM Role Configured

✔ Lambda Function Created

✔ Environment Variable Added

✔ IAM Policy Attached

✔ S3 Event Trigger Configured

✔ File Uploaded Successfully

✔ Lambda Triggered Automatically

✔ File Copied to Destination Bucket

---

## 📚 Learning Outcomes

- Amazon S3
- AWS Lambda
- IAM Roles & Policies
- S3 Event Notifications
- CloudWatch Logs
- Serverless Architecture
- Event-Driven Automation

---

## 👨‍💻 Author

**Sumedh Hiwale**

GitHub: https://github.com/sumedh-hiwale

---
⭐ If you found this project useful, consider giving it a star!
