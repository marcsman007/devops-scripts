#!/bin/bash
# Backup files to S3
# Usage: ./backup-to-s3.sh /path/to/folder bucket-name

SOURCE_DIR=$1
BUCKET_NAME=$2
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

if [ -z "$SOURCE_DIR" ] || [ -z "$BUCKET_NAME" ]; then
  echo "Usage: $0 /path/to/folder bucket-name"
  exit 1
fi

echo "Backing up $SOURCE_DIR to s3://$BUCKET_NAME/backup_$TIMESTAMP ..."
aws s3 cp --recursive "$SOURCE_DIR" "s3://$BUCKET_NAME/backup_$TIMESTAMP"

if [ $? -eq 0 ]; then
  echo "Backup completed successfully!"
else
  echo "Backup failed!"
fi
