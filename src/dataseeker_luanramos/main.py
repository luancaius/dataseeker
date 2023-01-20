import requests
from src.dataseeker_luanramos.entity import RequestEntity, RequestTypeEnum


class DataSeeker:
    @staticmethod
    def create_request(url: str, metadata: dict):
        request = None
        if not url:
            raise Exception("Cant create a request without URL")
        if metadata is None:
            request = RequestEntity(url, RequestTypeEnum.REST, None, None)
        if metadata['type_request'] == 'REST':
            type_request = RequestTypeEnum.REST
            operation = metadata['operation']
            request = RequestEntity(url, type_request, operation, None)
        return request

    def __init__(self, request: RequestEntity):
        self.request = request

    def handle(self):
        response = None
        if self.request.type_request == RequestTypeEnum.REST:
            if self.request.operation == 'GET':
                response = requests.get(self.request.url, headers=self.request.headers)
        return response



