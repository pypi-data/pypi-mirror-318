from blockhouse.client.s3_connector import S3Connector
class Transfer:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.s3_connector = S3Connector(aws_access_key_id, aws_secret_access_key, region_name)

    def send_file(self, local_file_path, bucket_name):
        # Upload a file to an S3 bucket
        return self.s3_connector.upload_file(local_file_path, bucket_name)