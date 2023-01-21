import requests
from src.dataseeker_luanramos.entity import RequestEntity, TypeRequestEnum


class DataSeeker:
    @staticmethod
    def create_request(url: str, metadata: dict):
        request = None
        if not url:
            raise Exception("Cant create a request without URL")
        if metadata is None:
            request = RequestEntity(url, TypeRequestEnum.REST, None, None)
        if metadata['type_request'] == 'REST':
            type_request = TypeRequestEnum.REST
            operation = metadata.get('operation', None)
            body = metadata.get('body', None)
            request = RequestEntity(url, type_request, operation, body)
        return request

    def __init__(self, request: RequestEntity):
        self.request = request

    def handle(self):
        response = None
        if self.request.type_request == TypeRequestEnum.REST:
            if self.request.operation == 'GET':
                response = requests.get(self.request.url, headers=self.request.headers)
            elif self.request.operation == 'POST':
                body = self.request.body
                response = requests.post(self.request.url, headers=self.request.headers, json=body)
        return response



