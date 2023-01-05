from enum import Enum


class RequestTypeEnum(Enum):
    REST = 0
    SOAP = 1
    GRPC = 2


class RequestEntity:
    def __init__(self, url: str, request_type: RequestTypeEnum, headers: dict, body: str):
        self.url = url
        self.request_type = request_type
        self.header = headers
        self.body = body
