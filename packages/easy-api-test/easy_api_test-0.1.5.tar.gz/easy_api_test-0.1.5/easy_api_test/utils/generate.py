import os
import ast
import json
from pathlib import Path
from collections import defaultdict
from pprint import pformat
import re
from urllib.parse import urlparse, parse_qsl
from easy_api_test.utils.parser import CURLParser

tmp1 = """
    def %(funcName)s(self, **kwargs):
        '''
        kwargs example: %(body)s
        '''
        url = '%(url)s'
        body = %(body)s
        body.update(kwargs)
        self.client.%(method)s(url, json=body)
        return self.client.get_response_data()
"""
tmp11 = """
    def %(funcName)s(self, **kwargs):
        '''
        kwargs example: %(body)s
        '''
        url = '%(url)s'
        body = %(body)s
        body.update(kwargs)
        self.client.%(method)s(url, data=body)
        return self.client.get_response_data()
"""
tmp12 = """
    def %(funcName)s(self, **kwargs):
        '''
        kwargs example: %(body)s
        '''
        url = '%(url)s'
        body = %(body)s
        body.update(kwargs)
        self.client.%(method)s(url, data=body, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        return self.client.get_response_data()
"""

tmp2 = """
    def %(funcName)s(self, **kwargs):
        url = '%(url)s'
        params = %(params)s
        params.update(kwargs)
        self.client.%(method)s(url, params=params)
        return self.client.get_response_data()
"""

tmp3 = """
    def %(funcName)s(self):
        url = '%(url)s'
        self.client.%(method)s(url)
        return self.client.get_response_data()
"""
tmp4 = """
    def %(funcName)s(self, params=None, data=None, headers=None):
        '''
        params example: %(params)s
        data example: %(data)s
        headers example: %(headers)s
        '''
        url = '%(url)s'
        params = params or %(params)s
        data = data or %(data)s
        headers = headers or %(headers)s
        self.client.%(method)s(url, params=params, data=data, headers=headers)
        return self.client.get_response_data()
"""

def convert_to_snake_case(name):
    """
    将不规则命名转换为蛇形命名。

    参数:
    name (str): 要转换的原始命名字符串。

    返回:
    str: 转换后的蛇形命名字符串。
    """
    # 首先将字符串中的非字母数字字符替换为下划线，并处理连续多个下划线的情况
    s1 = re.sub(r'[^\w]', '_', name)
    s2 = re.sub(r'_{2,}', '_', s1)
    # 然后将字符串中大写字母转换为小写，并在其前面添加下划线（除了首字母大写情况）
    s3 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s2).lower()
    # 去除开头和结尾可能多余的下划线
    return s3.strip('_')

def convert_to_camel_case(name):
    """
    将名称转换为驼峰命名。
    """
    words = convert_to_snake_case(name).split('_')
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])

def url_to_structure(url, ignore_num=0, path_num=1, file_num=1):
    """
    将URL路径按照给定规则转换为目录结构、文件名和方法名。

    参数:
    url (str): 要转换的URL路径字符串
    ignore_num (int): 忽略的最前面路径段的数量
    path_num (int): 转换为目录的路径段数量
    file_num (int): 转换为文件名的路径段数量

    返回:
    tuple: (目录列表, 文件名, 方法名)

    示例:
    >>> url_to_structure('/api/trade/order/create/v2', 1, 1, 1)
    (['trade'], 'order', 'createV2')
    """
    # 分割并清理URL路径
    parts = [p for p in url.strip('/').split('/') if p]
    
    # 检查路径段是否足够
    if ignore_num >= len(parts):
        return [], "", ""
    
    # 去除要忽略的部分
    parts = parts[ignore_num:]
    
    # 提取目录部分
    directories = []
    for i in range(path_num):
        if i < len(parts) - 2:  # 至少保留2个路径段，用作文件名
            directories.append(convert_to_snake_case(parts[i]))
    
    # 提取文件名部分
    file_names = []
    for i in range(file_num):
        index = len(directories) + i
        if index < len(parts) - 1:  # 至少保留1个路径段，用作方法名
            file_names.append(convert_to_snake_case(parts[index]))
    # 处理剩余部分作为方法名
    method_parts = parts[len(directories) + len(file_names):]
    file_name = '_'.join(file_names) if file_names else 'index'
    method_name = ""
    for part in method_parts:
        if '.' in part:
            raise ValueError('包含非法字符 \'.\'，跳过。')
        method_name += convert_to_snake_case(part)
    method_name = method_name[0].lower() + method_name[1:]
    return directories, file_name, method_name


def generate_api_code(parser: CURLParser, ignore_num=0, path_num=1, file_num=1) -> tuple[list[str], str, str, str]:
    """
    生成API代码

    :param url: 请求URL
    :param method: 请求方法
    :param body: 请求体
    :param ignore_num: 忽略的层级，默认0
    :param path_num: 路径层级，默认1
    :param file_num: 文件层级，默认1
    """
    URL = urlparse(parser.url)
    try:
        directories, file_name, method_name = url_to_structure(URL.path, ignore_num, path_num, file_num)
    except Exception as e:
        print(f'解析URL{URL.path!r}异常：{e}')
        return [], '', '', ''
    params = None 
    if URL.query:
        params = parse_qsl(URL.query)

    if not parser.data and not params:
        code = tmp3 % dict(funcName=method_name, url=URL.path, method=parser.method.lower())
    elif parser.data and params:
        code = tmp4 % dict(funcName=method_name, url=URL.path, params=pformat(params, sort_dicts=False), data=pformat(parser.data, sort_dicts=False), headers={"Content-Type": parser.headers.get('content-type', '')}, method=parser.method.lower())
    elif params:
        code = tmp2 % dict(funcName=method_name, url=URL.path, params=pformat(params, sort_dicts=False), method=parser.method.lower())
    elif parser.headers.get('content-type', '').startswith('application/x-www-form-urlencoded'):
        code = tmp12 % dict(funcName=method_name, url=URL.path, body=pformat(parser.data, sort_dicts=False), method=parser.method.lower())
    elif parser.headers.get('content-type', '').startswith('multipart/form-data'):
        code = tmp11 % dict(funcName=method_name, url=URL.path, body=pformat(parser.data, sort_dicts=False), method=parser.method.lower())
    else:
        code = tmp1 % dict(funcName=method_name, url=URL.path, body=pformat(parser.data, sort_dicts=False), method=parser.method.lower())
    return directories, file_name, method_name, code


def split_curl_file(file_path: str | os.PathLike):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    with open(file_path, 'r', encoding='utf-8') as f:
        yield from iter(f.read().split('&\n'))


def generate_api_code_from_curl_file(file_path: str | os.PathLike, ignore_num, path_num, file_num):
    for curl in split_curl_file(file_path):
        parser = CURLParser(curl.replace('^', '').replace('\\', '').strip())
        if not parser.url:
            continue
        yield generate_api_code(parser, ignore_num, path_num, file_num)  


def add_functions_to_class(file_path, class_name, functions):
    """
    在给定Python文件中，向指定类添加函数（如果类不存在则创建类），同时避免添加重复函数。

    :param file_path: Python文件的路径。
    :param class_name: 要添加函数的目标类名。
    :param functions: 要添加到类中的函数列表，函数以函数对象形式传入。
    """
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('from ._base import _BaseAPI\n\nclass %s(_BaseAPI):\n' % class_name)
            for func_name, func_str in functions:
                file.write(func_str)
        return 
    with open(file_path, encoding='utf-8') as file:
        source_code = file.read()

    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        print(f"文件 {file_path} 存在语法错误，请检查后再试。")
        return

    class_defs = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef) and node.name == class_name]

    if class_defs:
        existing_function_names = []
        target_class = class_defs[0]
        for node in ast.walk(target_class):
            if isinstance(node, ast.FunctionDef):
                existing_function_names.append(node.name)

        for func_name, func_str in functions:
            if func_name not in existing_function_names:
                func_ast = ast.parse(func_str).body[0]
                target_class.body.append(func_ast)
            else:
                print(f"函数 {func_name} 已存在于类 {class_name} 中，跳过添加。")
    else:
        new_class_ast = ast.ClassDef(class_name, bases=[], keywords=[], body=[], decorator_list=[], type_params=[])
        for func_name, func_str in functions:
            func_ast = ast.parse(func_str).body[0]
            new_class_ast.body.append(func_ast)
        tree.body.append(new_class_ast)

    updated_source = ast.unparse(tree)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_source)


def _make_init_file(path: Path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        with open(path / '__init__.py', 'w', encoding='utf-8') as f:
            f.write('')
        with open(path / '_base.py', 'w', encoding='utf-8') as f:
            f.write('from .._base import API\n\nclass _BaseAPI(API):\n    pass')


def generate_api_file(file_path: str | os.PathLike, output_path: str | os.PathLike, ignore_num=0, path_num=1, file_num=1):
    data = defaultdict(dict)
    base_path = Path(output_path)
    _make_init_file(base_path)
    for directories, file_name, funcName, code in generate_api_code_from_curl_file(file_path, ignore_num, path_num, file_num): 
        if not code:
            continue
        path = base_path
        for dir_name in directories:
            path = path / dir_name
            _make_init_file(path)
        else:
            path = path / f'{file_name}.py'
        data[path][funcName] = code

    for path, insert_codes in data.items():
        className = ''.join(n[0].upper() + n[1:] for n in path.stem.split('_')) + 'API'
        add_functions_to_class(path, className, insert_codes.items())


class GenerateAPI:
    """
    生成API数据

    :params file_path: 输入的curl文件路径
    :params output_path: 输出的API文件路径
    :params ignore_num: 忽略的层级，默认0
    :params path_num: 路径层级，默认1，连续path_num个路径会生成path_num层目录
    :params file_num: 文件层级，默认1，连续file_num个路径拼接并生成文件

    示例：
    >>> GenerateAPI('./data/curl.txt', './apis').start(ignore_num=0, path_num=1, file_num=1)

    生成文件结构：
    ./apis/
        __init__.py
        _base.py
        psm_platform_user/
            __init__.py
            oauth.py
    """

    def __init__(self, file_path: str | os.PathLike, output_path: str | os.PathLike) -> None:
        self.file_path = file_path
        self.output_path = output_path

    def start(self, ignore_num=0, path_num=1, file_num=1):
        """
        开始生成API

        :params ignore_num: 忽略的层级，默认0
        :params path_num: 路径层级，默认1，连续path_num个路径会生成path_num层目录
        :params file_num: 文件层级，默认1，连续file_num个路径拼接并生成文件
        """
        generate_api_file(self.file_path, self.output_path, ignore_num, path_num, file_num)

if __name__ == '__main__':
    generate_api_file('./easy_api_test/utils/curl.txt', './easy_api_test/apis')
    