from enum import Enum


class TypeRequestEnum(Enum):
    REST = 0
    SOAP = 1
    GRPC = 2
    GRAPHQL = 3


class RequestEntity:
    def __init__(self, url: str, type_request: TypeRequestEnum, operation: str,  headers: dict, body: str = None):
        self.url = url
        self.type_request = type_request
        self.operation = operation
        self.headers = headers
        self.body = body

