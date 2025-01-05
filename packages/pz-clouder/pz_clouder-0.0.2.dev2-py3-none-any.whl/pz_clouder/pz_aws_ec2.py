# this file contains code of inference process initiation
from src.pz_clouder.pz_aws_master import AWSMaster


class EC2ClientPZ(AWSMaster):
    def __init__(self):
        super().__init__()
        self.client = self.session.client("ec2")

    def create_ec2_instance(self, **kwrags):
        """:param kwrags:
        - ImageId (string)
        - InstanceType (string but should be default)
        - KeyName (string should be default)
        = SecurityGroupIds (list)
        - local_server_data_directory - directory that will be created in Ec2 server and wil, contains all config filer
        """
        instance_params = {
            "ImageId": kwrags.get("ImageId"),
            "InstanceType": kwrags.get("InstanceType"),
            "KeyName": kwrags.get("KeyName"),
            "SecurityGroupIds": kwrags.get("SecurityGroupIds"),
            "SubnetId": kwrags.get("SubnetId"),
            "MinCount": 1,
            "MaxCount": 1,
            "IamInstanceProfile": kwrags.get("IamInstanceProfile"),
            "UserData": kwrags.get("UserData"),
        }

        response = self.client.run_instances(**instance_params)
        waiter = self.client.get_waiter("instance_running")
        instance = response["Instances"][0]
        instance_id = instance["InstanceId"]
        waiter.wait(InstanceIds=[instance_id])
        return instance_id

    def terminate_ec2_instance(self, instance_id):
        self.client.terminate_instances(InstanceIds=[instance_id])
        waiter = self.client.get_waiter("instance_terminated")
        waiter.wait(InstanceIds=[instance_id])

    def is_instance_exists(self, instance_id):
        try:
            response = self.client.describe_instances(InstanceIds=[instance_id])
            return len(response["Reservations"]) > 0
        except Exception:
            return False
