# This file conatisn wrapper of cloud watch functionality

import logging

import watchtower

from src.pz_clouder.pz_aws_master import AWSMaster


class CloudWatchClientPZ(AWSMaster):
    def __init__(self, log_group_name=None, log_stream_name=None):
        super().__init__()
        self.cloudwatch = self.session.client("logs")

        self._set_group_and_stream(log_group_name, log_stream_name)

    def _set_group_and_stream(self, log_group_name=None, log_stream_name=None):
        if log_group_name:
            self.log_group_name = log_group_name
        if log_stream_name:
            self.log_stream_name = log_stream_name

    def init_cloudwatch_objects(self, log_group_name=None, log_stream_name=None):
        self._set_group_and_stream(log_group_name, log_stream_name)
        try:
            self.cloudwatch.create_log_group(logGroupName=self.log_group_name)
        except self.cloudwatch.exceptions.ResourceAlreadyExistsException:
            pass
        try:
            self.cloudwatch.create_log_stream(
                logGroupName=self.log_group_name,
                logStreamName=self.log_stream_name,
            )
        except self.cloudwatch.exceptions.ResourceAlreadyExistsException:
            pass

    def init_logger(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.NOTSET)

    def init_watcher(self, log_group_name=None, log_stream_name=None):
        self._set_group_and_stream(log_group_name, log_stream_name)
        self.cw_handler = watchtower.CloudWatchLogHandler(
            log_group_name=self.log_group_name,
            log_stream_name=self.log_stream_name,
            boto3_client=self.cloudwatch,
            send_interval=0,
        )
        self.cw_handler.setLevel(logging.NOTSET)
        self.logger.addHandler(self.cw_handler)

    def get_log_events(self, log_group_name, log_stream_name):
        response = self.cloudwatch.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
        )
        return response

    def get_last_log_entry(self, log_group_name, log_stream_name):
        response = self.cloudwatch.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            limit=1,
            startFromHead=False,
        )
        if response.get("events"):
            return response.get("events")[0]
        return None

    def get_all_logs(self, log_group_name, log_stream_name):
        response = self.cloudwatch.get_log_events(
            logGroupName=log_group_name,
            logStreamName=log_stream_name,
            startFromHead=True,
        )
        return response
