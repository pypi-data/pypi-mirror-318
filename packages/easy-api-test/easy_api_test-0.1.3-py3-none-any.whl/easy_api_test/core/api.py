

from .http_client import HTTPClient


class API:
    
    
    def __init__(self, http_client: HTTPClient):
        self.client = http_client
