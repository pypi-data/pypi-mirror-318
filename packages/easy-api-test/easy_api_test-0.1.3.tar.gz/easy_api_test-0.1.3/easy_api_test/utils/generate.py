import os
import ast
import json
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlparse, parse_qsl

tmp1 = """
    def %(funcName)s(self, **kwargs):
        url = '%(url)s'
        body = %(body)s
        body.update(kwargs)
        self.client.%(method)s(url, json=body)
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




def generate_api_code(url, method, body):
    URL = urlparse(url)
    url_path = [i for i in URL.path.split('/') if i]
    dir_name = ''
    file_name = 'index.py'
    if len(url_path) > 2:
        dir_name = url_path[0]
        file_name = f'{url_path[1].replace("-", "_")}.py'
        url_path = url_path[2:]

    elif len(url_path) == 2:
        file_name = f'{url_path[0].replace("-", "_")}.py'
        url_path = url_path[1:]
    elif not url_path:
        url_path = ['index']
    dir_name = dir_name.replace('-', '_')
    names = ('_'.join(url_path)).replace('-', '_').split('_')
    name = names[0] + "".join((n[0].upper() + n[1:]) for n in names[1:])
    if '.' in name :
        return None, None, None, None
    body = body or {}
    if URL.query:
        body.update(parse_qsl(URL.query))
    

    if not body:
        return dir_name, file_name, name, tmp3 % dict(funcName=name, url=URL.path, method=method.lower())
    elif method.lower() == 'get':
        return dir_name, file_name, name, tmp2 % dict(funcName=name, url=URL.path, params=body, method='get')
    else:
        return dir_name, file_name, name, tmp1 % dict(funcName=name, url=URL.path, body=body, method=method.lower())

def parse_curl(curl: str):
    url: str = ''
    method: str = 'GET'
    body: dict | None = None
    for row in curl.replace('\\', '').replace('^', '').split('\n'):
        row = row.strip()
        if row.startswith('curl '):
            url = row[6:-1]
        elif row.startswith('-X '):
            method = row[4:-1]
        elif row.startswith('--data-raw '):
            v = row[12:-1]
            body = json.loads(v)
            method = 'POST'
    return url, method, body

def split_curl_file(file_path: str | os.PathLike):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    with open(file_path, 'r', encoding='utf-8') as f:
        yield from iter(f.read().split('&\n'))


def generate_api_code_from_curl_file(file_path: str | os.PathLike):
    for curl in split_curl_file(file_path):
        url, method, body = parse_curl(curl)
        if body:
            yield generate_api_code(url, method, body)  # type: ignore

def add_functions_to_class(file_path, class_name, functions):
    """
    在给定Python文件中，向指定类添加函数（如果类不存在则创建类），同时避免添加重复函数。

    :param file_path: Python文件的路径。
    :param class_name: 要添加函数的目标类名。
    :param functions: 要添加到类中的函数列表，函数以函数对象形式传入。
    """
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('from easy_api_test import API\n\nclass %s(API):\n' % class_name)
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


def generate_api_file(file_path: str | os.PathLike, output_path: str | os.PathLike):
    data = defaultdict(dict)
    for dir_name, file_name, funcName, code in generate_api_code_from_curl_file(file_path): 
        if not code:
            continue
        path = Path(os.path.join(output_path, dir_name, file_name))  # type: ignore
        data[path][funcName] = code

    for path, insert_codes in data.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        className = ''.join(n[0].upper() + n[1:] for n in path.stem.split('_')) + 'API'
        add_functions_to_class(path, className, insert_codes.items())


if __name__ == '__main__':
    generate_api_file(r'./tests/d.txt', r'./tests')