import os

import boto3
from dotenv import load_dotenv

load_dotenv()
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
aws_session_token = os.getenv("aws_session_token")


class AWSMaster:
    def __init__(self):
        if aws_access_key_id is None:
            self.session = boto3.Session()
        else:
            self.session = boto3.Session(
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                aws_session_token=aws_session_token,
                region_name="eu-central-1",
            )
