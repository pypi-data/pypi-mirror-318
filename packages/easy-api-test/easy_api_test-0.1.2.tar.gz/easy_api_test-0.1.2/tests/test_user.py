import pytest

from easy_api_test import API, HTTPClient
from easy_api_test.utils import p

class MyClient(HTTPClient):
    pass 
class LoginAPI(API):
    def login(self, username: str, password: str):
        pass 



class UserManageAPI(API):
    def create_user(self, user_info: dict):
        pass  

    def delete_user(self, user_id: str):
        pass 

class TestUser:
    def setup_class(self):
        client = MyClient('http://tshirt-test.riin.com')
        self.login_api = LoginAPI(client)
        self.user_api = UserManageAPI(client)
    
    def test_create_user(self):
        # 先登录
        self.login_api.login("admin", "password")
        
        # 创建用户
        user_info = {
            "name": "test_user",
            "email": "test@example.com"
        }
        response = self.user_api.create_user(user_info)
    
    @pytest.mark.parametrize("user_id", *p(
            ('一般用户', 1),
            ('管理员', 2)
    ))
    def test_delete_user(self, user_id: str):
        pass 
