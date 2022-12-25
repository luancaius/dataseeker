from src.enum.enum_request_type import EnumRequestType


class Request:
    def __init__(self, enum_request_type: EnumRequestType, raw_url: str):
        self.request_type = enum_request_type
        self.raw_url = raw_url

