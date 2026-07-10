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
            "Bucket": source_bucket,
            "Key": key
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
