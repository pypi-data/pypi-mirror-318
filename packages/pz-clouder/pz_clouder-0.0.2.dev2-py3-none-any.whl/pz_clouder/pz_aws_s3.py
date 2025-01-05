# this code manage operations with S3
from src.pz_clouder.pz_aws_master import AWSMaster


class S3ClientPZ(AWSMaster):
    def __init__(self):
        super().__init__()
        self.s3 = self.session.client("s3")

    def create_folder(self, bucket_name, folder_name):
        self.s3.put_object(Bucket=bucket_name, Key=(folder_name + "/"))

    def upload_file(self, file_content, bucket_name, key):
        self.s3.put_object(Bucket=bucket_name, Key=key, Body=file_content)
