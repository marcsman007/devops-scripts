import boto3
import os
import logging
from botocore.exceptions import ClientError
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def upload_folder_to_s3(local_folder, bucket_name, s3_prefix="backup"):
    """
    Uploads all files in local_folder to the specified S3 bucket under s3_prefix.
    """
    s3_client = boto3.client('s3')
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_folder)
            s3_path = f"{s3_prefix}/{datetime.now().strftime('%Y%m%d_%H%M%S')}/{relative_path}"
            try:
                s3_client.upload_file(local_path, bucket_name, s3_path)
                logger.info(f"Uploaded {local_path} to s3://{bucket_name}/{s3_path}")
            except ClientError as e:
                logger.error(f"Failed to upload {local_path}: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Backup local folder to S3")
    parser.add_argument("--local", required=True, help="Local folder to backup")
    parser.add_argument("--bucket", required=True, help="S3 bucket name")
    parser.add_argument("--prefix", default="backup", help="S3 folder prefix")
    args = parser.parse_args()

    upload_folder_to_s3(args.local, args.bucket, args.prefix)
