import boto3
from botocore.exceptions import NoCredentialsError

from starcraft_data_orm.storage.storage import Storage

class S3Storage(Storage):
    def __init__(self, bucket_name: str, region_name: str = "us-east-1"):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client("s3", region_name=region_name)

    def upload(self, source_path: str, destination_path: str) -> None:
        try:
            self.s3_client.upload_file(source_path, self.bucket_name, destination_path)
            print(f"Uploaded to S3: {self.bucket_name}/{destination_path}")
        except NoCredentialsError:
            print("S3 credentials not available")
            raise

    def download(self, source_path: str, destination_path: str) -> None:
        try:
            self.s3_client.download_file(self.bucket_name, source_path, destination_path)
            print(f"Downloaded from S3: {self.bucket_name}/{source_path}")
        except NoCredentialsError:
            print("S3 credentials not available")
            raise

