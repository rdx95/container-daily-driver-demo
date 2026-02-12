import boto3
from fastapi import UploadFile
import os
from uuid import uuid4

S3_ENDPOINT = os.environ["S3_ENDPOINT"]
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
S3_BUCKET = "uploads"

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url=S3_ENDPOINT,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

# Create bucket if not exists
try:
    s3.head_bucket(Bucket=S3_BUCKET)
except:
    s3.create_bucket(Bucket=S3_BUCKET)

async def upload_file_to_s3(file: UploadFile):
    file_id = f"{uuid4()}_{file.filename}"
    content = await file.read()
    s3.put_object(Bucket=S3_BUCKET, Key=file_id, Body=content)
    return f"{S3_ENDPOINT}/{S3_BUCKET}/{file_id}"
