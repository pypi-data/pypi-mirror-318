from .http_client import HTTPClient


class API[T:HTTPClient]:
    
    
    def __init__(self, http_client: T):
        self.client = http_client

