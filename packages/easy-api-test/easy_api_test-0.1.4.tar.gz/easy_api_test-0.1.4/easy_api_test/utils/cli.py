import pathlib
from lljz_tools.color import Color
from ..core.logger import logger
import easy_api_test

config_template = """base_url: {base_url}
timeout: 60
username: admin
password: 123456
tester: 机智的测试员
project_name: {project_name}"""

requirements_template = f"""easy_api_test=={easy_api_test.__version__}
pytest-testreport>=1.1.6
jinja2==3.1.5"""

case_runner = """import pytest
import os
import re
from lljz_tools.color import Color
from easy_api_test.utils import Data
from core.config import settings


args = [
    './test_case',
    f'--report=_report.html',
    f'--title={settings.project_name}自动化测试报告',
    f'--tester={settings.tester}',
    '--desc=基于接口自动化的测试报告',
    '--template=2',
]
pytest.main(args)
lastFile = ''
for file in os.listdir('./reports'):
    path = os.path.join('./reports', file)
    if not os.path.isfile(path) or not file.endswith('.html'):
        continue
    lastFile = path
if lastFile:
    print()
    print(Color.green("测试用例执行完成！测试报告地址如下："))
    print(f"    {Color.color(os.path.abspath(lastFile), style='u blue')}")
    print()
    with (
        open(Data.jquery, 'r', encoding='utf-8') as jquery,
        open(Data.echarts, 'r', encoding='utf-8') as echarts,
        open(Data.bootstrap, 'r', encoding='utf-8') as bootstrap,
        open(lastFile, 'r+', encoding='utf-8') as f
    ):
        jqueryContent = jquery.read()
        echartsContent = echarts.read()
        bootstrapContent = bootstrap.read()
        content = f.readlines()
        # print(*content[6:9])
        content[6] = f'<style>{bootstrapContent}</style>\\n'
        content[7] = f'<script>{jqueryContent}</script>\\n'
        content[8] = f'<script>{echartsContent}</script>\\n'
    with open(lastFile, 'w', encoding='u8') as f:
        content = ''.join(content)
        content = re.sub(r'\\[\\d{1,3}m', '', content)
        f.write(''.join(content))"""

gitignore = """.idea/
.vscode/
.git/
.venv/
__pycache__/
config.yaml
logs/
scripts/
reports/*.html
.pytest_cache/
"""

tools = """from core.config import Path
from easy_api_test.utils import generate_api_file as _generate_api_file

def generate_api_file():
    _generate_api_file(file_path=Path.CURLS_FILE, output_path=Path.ROOT / "apis")
"""

test_index = """import pytest
from easy_api_test.utils import p

from core.client import HTTPClient
from core.config import settings
from apis.index import IndexAPI


class TestIndex:

    def setup_class(self):
        self.client = HTTPClient().login(settings.username, settings.password)
        self.api = IndexAPI(self.client)

    @pytest.mark.parametrize('params', **p(
            ("正常访问", "abc1"),
            ("异常访问", "abc2"),
    ))
    def test_index(self, params):
        self.client.get('/')
        self.client.get_response_data()
    
    @pytest.mark.skip(reason="跳过")
    def test_index2(self):
        pass

if __name__ == "__main__":
    import pytest
    pytest.main(['-s', '-v', 'test_case/test_index.py'])
"""
base = """from easy_api_test import Model

class UserInfo(Model):
    id: int 
    username: str """
client = """from logging import Logger
from easy_api_test import HTTPClient as _HTTPClient

from core.config import settings
from core.logger import logger
from schemas.base import UserInfo

class HTTPClient(_HTTPClient):

    def __init__(self, base_url: str | None = None, *, timeout: int = 0, debug: bool | Logger = True):
        debug = logger if debug is True else debug
        super().__init__(base_url=base_url or settings.base_url, timeout=timeout or settings.timeout, debug=debug)

    def login(self, username: str, password: str):
        # TODO: 完善登录功能
        # self.post('/auth/token', json={'username': username, 'password': password})
        
        # 将token添加到headers中
        # data = self.get_response_data()
        # self.headers['Authorization'] = f'Bearer {data["token"]}'

        # 获取用户的基本信息
        # self.get('/auth/user/info')
        # self.userInfo = UserInfo(**data)
        return self
"""
config = """from easy_api_test import BaseSettings
from pathlib import Path as _Path

class Path:
    ROOT = _Path(__file__).parent.parent
    CONFIG_FILE = ROOT / "config.yaml"
    LOGS_DIR = ROOT / "logs"
    CURLS_FILE = ROOT / "data" / "curls.txt"

class Settings(BaseSettings):
    base_url: str
    timeout: int
    username: str 
    password: str 
    tester: str = 'Unknown'
    project_name: str = '一个项目'


settings = Settings.load_from_yaml_file(Path.CONFIG_FILE)

if __name__ == "__main__":
    print(settings)

"""
log = """from easy_api_test import init_logger

from core.config import Path

logger = init_logger('DEBUG', 'DEBUG', file_path=str(Path.LOGS_DIR))"""

index = """from easy_api_test import API

class IndexAPI(API):

    def index(self):
        self.client.get('/')
        return self.client.get_response_data()
"""

def cli():
    base_path = pathlib.Path('.').absolute()
    print(Color.blue('欢迎使用EasyApiTest'))
    print('请输入项目名称', Color.color('（默认：XX项目）', style='i u thin_white'))
    project_name = input(':').strip() or 'XX项目'
    print('你的项目名称为：', Color.color(project_name, style='u thin_yellow'))
    print('请输入测试环境地址', Color.color('（默认：http://localhost:8000）', style='i u thin_white'))
    base_url = input(':').strip() or 'http://localhost:8000'
    print('你的测试环境地址为：', Color.color(base_url, style='u thin_yellow'))
    try:
        config_str = config_template.format(base_url=base_url, project_name=project_name)
        with open(base_path / 'config.yaml', 'w', encoding='utf-8') as f:
            f.write(config_str)
        with open(base_path / 'config.example.yaml', 'w', encoding='utf-8') as f:
            f.write(config_str)
        with open(base_path / 'requirements.txt', 'w', encoding='utf-8') as f:
            f.write(requirements_template)
        with open(base_path / 'start.py', 'w', encoding='utf-8') as f:
            f.write(case_runner)
        with open(base_path / '.gitignore', 'w', encoding='utf-8') as f:
            f.write(gitignore)
        utils = base_path / 'utils'
        utils.mkdir(parents=True, exist_ok=True)
        with open(utils / '__init__.py', 'w', encoding='utf-8') as f:
            f.write('')
        with open(utils / 'tools.py', 'w', encoding='utf-8') as f:
            f.write(tools)
        test_case = base_path / 'test_case'
        test_case.mkdir(parents=True, exist_ok=True)
        with open(test_case / '__init__.py', 'w', encoding='utf-8') as f:
            f.write('')
        with open(test_case / 'test_index.py', 'w', encoding='utf-8') as f:
            f.write(test_index)
        schemas = base_path / 'schemas'
        schemas.mkdir(parents=True, exist_ok=True)
        with open(schemas / '__init__.py', 'w', encoding='utf-8') as f:
            f.write('')
        with open(schemas / 'base.py', 'w', encoding='utf-8') as f:
            f.write(base)
        reports = base_path / 'reports'
        reports.mkdir(parents=True, exist_ok=True)
        logs = base_path / 'logs'
        logs.mkdir(parents=True, exist_ok=True)
        data = base_path / 'data'
        data.mkdir(parents=True, exist_ok=True)
        with open(data / 'curls.txt', 'w', encoding='utf-8') as f:
            f.write('')
        core = base_path / 'core'
        core.mkdir(parents=True, exist_ok=True)
        with open(core / '__init__.py', 'w', encoding='utf-8') as f:
            f.write('')
        with open(core / 'config.py', 'w', encoding='utf-8') as f:
            f.write(config)
        with open(core / 'logger.py', 'w', encoding='utf-8') as f:
            f.write(log)
        with open(core / 'client.py', 'w', encoding='utf-8') as f:
            f.write(client)
        apis = base_path / 'apis'
        apis.mkdir(parents=True, exist_ok=True)
        with open(apis / '__init__.py', 'w', encoding='utf-8') as f:
            f.write('')
        with open(apis / 'index.py', 'w', encoding='utf-8') as f:
            f.write(index)
    except Exception as e:
        logger.exception(f'项目创建失败：{e}')
    else:
        print()
        print(Color.green('项目创建成功！'), '请执行下面的命令：')
        print()
        print('\t', Color.blue("pip install -r requirements.txt"), Color.color(' # 安装依赖', style='i cyan'))
        print('\t', Color.blue("python -m start"), Color.color('                 # 运行测试用例', style='i cyan'))
        print()