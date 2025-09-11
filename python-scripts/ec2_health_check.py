import boto3
import logging
from botocore.exceptions import ClientError

# Set up Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_ec2_health(region='ap-southeast-1'):
    ec2_client = boto3.client('ec2', region_name=region)
    try:
        # Describe EC2 instances
        response = ec2_client.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                logger.info(f"Instance ID: {instance_id}, State: {state}")
                if state != 'running':
                    logger.warning(f"Instance {instance_id} is not running!")
    except ClientError as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    check_ec2_health()
