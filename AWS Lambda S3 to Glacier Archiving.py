import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = 'primary-bucket-1212'
    destination_bucket = 'snap-bucket-1212'

    source_key = event['Records'][0]['s3']['object']['key']

    destination_key = f'archived/{source_key}'  # You can customize the destination path

    s3_client.copy_object(
        Bucket=destination_bucket,
        CopySource={'Bucket': source_bucket, 'Key': source_key},
        Key=destination_key,
        StorageClass='DEEP_ARCHIVE'
    )

    print(f'Object archived: s3://{destination_bucket}/{destination_key}')

    return {
        'statusCode': 200,
        'body': 'Object archived successfully!'
    }
