from typing import Union
from . import AWSService
from ..utils.common import remove_none_values


class S3(AWSService):
    __servicename__ = 's3'
    
    def get_objects_by_bucket_name(self, bucket_name, continuation_token = None):
        request_params = remove_none_values({
            "Bucket":bucket_name,
            'ContinuationToken': continuation_token
        })
        return self.client.list_objects_v2(**request_params)
    
    def list_objects_v2_with_paginator(self, bucket:str):
        return self.get_result_from_paginator('list_objects_v2', 'Contents', Bucket = bucket)

    def get_object(self, s3_path:str) -> bytes:
        bucket_name, key_name = get_bucket_and_key(s3_path)
        response = self.client.get_object(Bucket=bucket_name, Key=key_name)
        return response["Body"].read()
    
    def put_object(self, s3_path:str, body:Union[bytes,str]):
        bucket_name, key_name = get_bucket_and_key(s3_path)
        if isinstance(body,str):
            body = body.encode('utf-8')
        self.client.put_object(Bucket=bucket_name, Key=key_name, Body=body)

def get_bucket_and_key(s3_path:str):
    parts = s3_path.removeprefix('/').split('/',1)
    bucket_name = parts[0]
    key_name = parts[1] if len(parts) > 1 else ""

    return bucket_name, key_name