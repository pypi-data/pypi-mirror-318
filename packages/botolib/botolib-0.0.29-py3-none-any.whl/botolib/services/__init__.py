from abc import ABC
import itertools
from boto3.session import Session
import boto3
from ..utils.common import remove_none_values

_available_services = Session().get_available_services()

class AWSService(ABC):
    __servicename__ = None

    def __init__(self, session:Session = None):
        sn = self.__servicename__

        if sn not in _available_services:
            raise Exception(f"Service {sn} is not available")
        
        self.client = session.client(sn) if session is not None else boto3.client(sn)

    def __getattr__(self, name):
        if hasattr(self.client, name):
            return getattr(self.client, name)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")


    def _get_all_with_callback(self, get_list_function, result_token_name, next_token_name, callback_function, *args, next_token = None):
        results = []
        next_token = next_token
        has_next = True
        
        while has_next:
            response = get_list_function(*args, next_token)
            result = response.get(result_token_name)

            if callback_function:
                callback_function(result)
            else:
                if result is not None:
                    results.extend(result)
            next_token = response.get(next_token_name)
            has_next = next_token_name in response

        if not callback_function:
            return results
    
    def _get_all(self, get_list_function, result_token_name, next_token_name, *args):
        return self._get_all_with_callback(get_list_function, result_token_name, next_token_name, None, *args)
    
    def get_result_from_paginator(self, operation_name, result_token, callback_func = None, **kwargs):
        if 'PaginationConfig' not in kwargs:
            kwargs['PaginationConfig'] = {
                'PageSize': 50
            }

        self._gen_iterator = PageResultIterator(self.client, operation_name, kwargs, result_token)

        if callback_func is not None:
            for r in self._gen_iterator:
                callback_func(r)
        else:
            return list(itertools.chain(*self._gen_iterator))
        
    def paginate(self, func, **kwargs):
        if 'PaginationConfig' not in kwargs:
            kwargs['PaginationConfig'] = {
                'PageSize': 50
            }
        
        return PageResultIterator(self.client, getattr(func,"operation_name"), kwargs, getattr(func, "result_token"))
    
class PageResultIterator:
    def __init__(self, client, operation_name, kwargs, result_token):
        self._iterator = client.get_paginator(operation_name).paginate(**remove_none_values(kwargs))
        self._result_token = result_token
    
    def __iter__(self):
        for i in self._iterator:
            yield i.get(self._result_token, [])

def paginateable(operation_name, result_token):
    def decorator(func):
        setattr(func, "operation_name", operation_name)
        setattr(func, "result_token", result_token)
        return func
    return decorator