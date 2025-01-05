from src.pz_clouder.pz_aws_master import AWSMaster


class SQSClientPZ(AWSMaster):
    def __init__(self):
        super().__init__()
        self.sqs = self.session.client("sqs")

    def send_message(self, queue_url, message_body):
        self.sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)

    def consume_message(
        self,
        queue_url,
        visibility_timeout=500,
        wait_time=0,
        max_number_of_messages=1,
    ):
        response = self.sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=max_number_of_messages,
            VisibilityTimeout=visibility_timeout,
            WaitTimeSeconds=wait_time,
        )
        return response.get("Messages", [])

    def remove_message(self, queue_url, receipt_handle):
        self.sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
