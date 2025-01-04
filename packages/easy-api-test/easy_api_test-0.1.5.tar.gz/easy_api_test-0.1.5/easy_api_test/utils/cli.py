import pathlib
from lljz_tools.color import Color
from ..core.logger import logger
import easy_api_test

config_template = """base_url: {base_url}  # 测试环境地址
timeout: 60  # 请求超时时间
debug: True  # 是否开启调试默认，开启后将会自动记录请求的URL和参数
username: admin  # 用户名
password: 123456  # 密码
tester: 机智的测试员  # 测试员
project_name: {project_name}  # 项目名称"""

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
""" + "\n".join([
"        content[6] = f'<style>{bootstrapContent}</style>\\n' ",
"        content[7] = f'<script>{jqueryContent}</script>\\n' ",
"        content[8] = f'<script>{echartsContent}</script>\\n' ",
"    with open(lastFile, 'w', encoding='u8') as f:",
"        content = ''.join(content)",
"        content = re.sub(r'\\[\\d{1,3}m', '', content)",
"        f.write(''.join(content))",
])

gitignore = """.idea/
.vscode/
.git/
.venv/
__pycache__/
config.yaml
logs/
**/*.log
**/*.log.*
scripts/
reports/
.pytest_cache/
"""

tools = """from core.config import Path
from easy_api_test.utils.generate import GenerateAPI

def generate_api_file(ignore_num=0, path_num=1, file_num=1):
    '''
    生成API文件

    :params ignore_num: 忽略的层级，默认0
    :params path_num: 路径层级，默认1，连续path_num个路径会生成path_num层目录
    :params file_num: 文件层级，默认1，连续file_num个路径拼接并生成文件
    
    示例：
    >>> generate_api_file(ignore_num=0, path_num=1, file_num=1)
    '''
    g = GenerateAPI(file_path=Path.CURLS_FILE, output_path=Path.ROOT / "apis")
    g.start(ignore_num=ignore_num, path_num=path_num, file_num=file_num)

if __name__ == "__main__":
    generate_api_file(0, 1, 1)  # 忽略前面0个路径，生成1层目录，以1层路径拼接生成文件
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
base_schema = """from easy_api_test import Model

class UserInfo(Model):
    id: int 
    username: str """
client = """from logging import Logger
from easy_api_test import HTTPClient as _HTTPClient

from core.config import settings
from core.logger import logger
from schemas._base import UserInfo

class HTTPClient(_HTTPClient):

    def __init__(self, base_url: str = settings.base_url, *, timeout: int = settings.timeout, debug: bool | Logger = settings.debug):
        debug = logger if debug is True else debug
        super().__init__(base_url=base_url, timeout=timeout, debug=debug)
        self._userInfo: UserInfo | None = None
    
    @property
    def userInfo(self) -> UserInfo:
        if not self._userInfo:
            raise RuntimeError("请先登录并获取userInfo")
        return self._userInfo

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
    DATA_DIR = ROOT / "data"
    CURLS_FILE = DATA_DIR / "curls.txt"

class Settings(BaseSettings):
    base_url: str
    timeout: int
    debug: bool
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

base_api = """from easy_api_test import API as _API
from core.client import HTTPClient


class API(_API[HTTPClient]):

    def __init__(self, client: HTTPClient = HTTPClient()):
        super().__init__(client)

    def login(self, *args, **kwargs):
        self.client.login(*args, **kwargs)
        return self
"""

index_api = """from apis._base import API

class IndexAPI(API):

    def index(self):
        self.client.get('/')
        return self.client.get_response_data()
"""
pytest_ini = """[pytest]
disable_test_id_escaping_and_forfeit_all_rights_to_community_support = True
"""

readme = """> 欢迎使用easy_api_test自动化测试框架

## 框架目录结构

```
tshirt_auto/
├── README.md               # 项目说明文档
├── start.py               # 项目启动入口
├── .gitignore            # Git忽略文件配置
├── requirements.txt      # 项目依赖包文件
├── apis/                 # 接口定义目录
│   ├── __init__.py      
│   ├── _base.py            # 基础API类，所有的api都应该继承改基类
│   └── index.py           # 接口样例
├── core/                 # 核心功能目录
│   ├── __init__.py      
│   ├── logger.py        # 日志处理模块
│   ├── config.py        # 配置管理模块
│   └── client.py        # 请求客户端模块
├── data/                 # 数据目录
│   └── curls.txt        # curl命令数据文件
├── logs/                 # 日志目录
│   ├── out.log          # 输出日志文件
│   └── .__out.lock      # 日志文件锁
├── reports/             # 报告目录
│   └── history.json    # 历史记录JSON文件
├── schemas/            # 数据模型目录
│   ├── __init__.py    
│   └── _base.py      # 数据模型基类
├── test_case/         # 测试用例目录
│   ├── __init__.py    
│   └── test_*.py      # 测试用例文件
└── utils/             # 工具类目录
    ├── __init__.py    
    └── generate.py   # 数据生成工具
```

## 目录说明

1. **apis/** - 接口定义目录
   - `_base.py`: 基础API类，所有的api都应该继承改基类
   - `index.py`: 接口样例

2. **core/** - 核心功能目录
   - `__init__.py`: 核心模块的初始化文件，定义包级别的变量和导入
   - `logger.py`: 负责日志的收集、格式化和输出
   - `config.py`: 处理框架配置和环境变量
   - `client.py`: 封装HTTP请求客户端

3. **data/** - 测试数据目录
   - `curls.txt`: 存储curl格式的接口请求数据

4. **logs/** - 日志文件目录
   - `out.log`: 运行日志输出文件
   - `.__out.lock`: 日志文件锁，防止并发写入

5. **reports/** - 测试报告目录
   - `history.json`: 存储测试执行历史记录

6. **schemas/** - 数据模型目录，一般模型建议继承`easy_api_test.Model`基类
   - `_base.py`: 可以创建模型基类

7. **test_case/** - 测试用例目录
   - `test_*.py`: 各个模块的测试用例文件

8. **utils/** - 工具类目录
   - `generate.py`: 通过curls.txt文件内容自动生成API代码

9. **根目录文件**
   - `start.py`: 项目的启动入口文件
   - `.gitignore`: 配置Git版本控制需要忽略的文件
   - `requirements.txt`: 项目所需的Python依赖包列表

## 使用说明

1. **环境准备**
   ```bash
   pip install -r requirements.txt
   ```

2. **启动项目**
   ```bash
   python -m start
   ```

## 注意事项

1. 运行前请确保：
   - 已安装所有依赖包
   - logs目录具有写入权限
   - 配置文件参数正确

2. 日志管理：
   - 日志文件会自动按日期归档
   - 建议定期清理过期日志

3. 数据管理：
   - curl命令需按规定格式录入，可以在浏览器控制台中复制cURL命令获得

## 开发规范

1. 代码提交前：
   - 确保通过所有测试
   - 更新相关文档
   - 遵循.gitignore规则 
"""

def write_file(content: str, file_path: pathlib.Path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

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
        write_file(case_runner, base_path / 'start.py')
        config_str = config_template.format(base_url=base_url, project_name=project_name)
        write_file(readme, base_path / 'README.md')
        write_file(config_str, base_path / 'config.yaml')
        write_file(config_str, base_path / 'config.example.yaml')
        write_file(requirements_template, base_path / 'requirements.txt')
        write_file(gitignore, base_path / '.gitignore')
        utils = base_path / 'utils'
        utils.mkdir(parents=True, exist_ok=True)
        write_file('', utils / '__init__.py')
        write_file(tools, utils / 'generate.py')

        test_case = base_path / 'test_case'
        test_case.mkdir(parents=True, exist_ok=True)
        write_file('', test_case / '__init__.py')
        write_file(test_index, test_case / 'test_index.py')
        write_file(pytest_ini, test_case / 'pytest.ini')
        
        schemas = base_path / 'schemas'
        schemas.mkdir(parents=True, exist_ok=True)
        write_file('', schemas / '__init__.py')
        write_file(base_schema, schemas / '_base.py')
        
        reports = base_path / 'reports'
        reports.mkdir(parents=True, exist_ok=True)
        logs = base_path / 'logs'
        logs.mkdir(parents=True, exist_ok=True)
        data = base_path / 'data'
        data.mkdir(parents=True, exist_ok=True)
        write_file('', data / 'curls.txt')
        core = base_path / 'core'
        core.mkdir(parents=True, exist_ok=True)
        write_file("", core / '__init__.py')
        write_file(config, core / 'config.py')
        write_file(log, core / 'logger.py')
        write_file(client, core / 'client.py')
        apis = base_path / 'apis'
        apis.mkdir(parents=True, exist_ok=True)
        write_file("", apis / '__init__.py')
        write_file(base_api, apis / '_base.py')
        write_file(index_api, apis / 'index.py')
    except Exception as e:
        logger.exception(f'项目创建失败：{e}')
    else:
        print()
        print(Color.green('项目创建成功！'), '请执行下面的命令：')
        print()
        print('\t', Color.blue("pip install -r requirements.txt"), Color.color(' # 安装依赖', style='i cyan'))
        print('\t', Color.blue("python -m start"), Color.color('                 # 运行测试用例', style='i cyan'))
        print()