from src.enum.enum_type_request import EnumRequestType


class Request:
    def __init__(self, enum_type_request: EnumRequestType, raw_url: str):
        self.type_request = enum_type_request
        self.raw_url = raw_url

