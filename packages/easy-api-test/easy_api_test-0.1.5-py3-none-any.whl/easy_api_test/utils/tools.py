import datetime
from io import BytesIO
from pathlib import Path
from typing import Any, Callable, TypedDict
from lljz_tools.excel import ExcelWriter
from requests import Response
from requests.exceptions import JSONDecodeError
from jsonpath_ng import parse

class ParametrizeData[T](TypedDict):
    argvalues: list[T]
    ids: list[str]

type ParamsName = str

def p[T](*args: tuple[ParamsName, T]) -> ParametrizeData[T]:
    return ParametrizeData(argvalues=[d[1] for d in args], ids=[d[0] for d in args])


def get_time_range(start: int = 0, end: int = 0, start_key: str = 'startTime', end_key: str = 'endTime') -> dict[str, str]:
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=start)
    end_date = today - datetime.timedelta(days=end)
    return {start_key: f'{start_date} 00:00:00', end_key: f'{end_date} 23:59:59'}


def remove_null_values[T: Any](data: T) -> T:
    """
    移除字典或列表、元组、集合中的空值

    :param data: 字典或列表、元组、集合
    :return: 移除空值后的字典或列表、元组、集合
    """
    if isinstance(data, dict):
        return {k: remove_null_values(v) for k, v in data.items() if v is not None} # type: ignore
    elif isinstance(data, list | tuple | set):
        return type(data)(remove_null_values(v) for v in data)  # type: ignore
    else:
        return data

class AssertTools:

    @staticmethod
    def http_status_code(response: Response, status_code: int = 200, /, *, message: str = '', not_contains_message: str = '') -> None:
        if not message:
            try:
                data = response.json()
            except JSONDecodeError:
                message = response.text[:200]
            else:
                message = data.get('message', data.get('msg', data.get('Msg', data.get('Message', response.text[:200]))))
            if not_contains_message:
                assert not_contains_message not in message, f'message: {message}'
            
        assert response.status_code == status_code, f'status_code is {response.status_code} but expect {status_code}, message: {message}'

    @staticmethod
    def http_ok(response: Response, /, *, message: str = '', not_contains_message: str = '') -> None:
        AssertTools.http_status_code(response, 200, message=message, not_contains_message=not_contains_message)
            
    @staticmethod
    def get_error(response: Response, /, *, message: str = '', not_contains_message: str = '') -> None:
        AssertTools.http_status_code(response, 500, message=message, not_contains_message=not_contains_message)

    @staticmethod
    def get_error_without_system(response: Response, /, *, message: str = '', not_contains_message: str = '系统错误') -> None:
        """获取一次错误，但错误信息不包含“系统错误”"""
        AssertTools.http_status_code(response, 500, message=message, not_contains_message=not_contains_message)
    
    @staticmethod
    def accept_error(func: Callable, *args, not_contains_message: str = '', **kwargs) -> None:
        """期望方法执行失败，但错误信息不包含`not_contains_message`"""
        try:
            func(*args, **kwargs)
        except AssertionError as e:
            if not_contains_message:
                assert not_contains_message not in str(e), str(e)
        else:
            raise AssertionError(f'期望[{func.__name__}]执行失败，实际执行成功！')
    
    @staticmethod
    def accept_error_without_system(func: Callable, *args, not_contains_message: str = '系统错误', **kwargs) -> None:
        """期望方法执行失败，但错误信息不包含“系统错误”"""
        AssertTools.accept_error(func, *args, not_contains_message=not_contains_message, **kwargs)

    @staticmethod
    def assert_json_value(data: Any, json_path: str, expect_value: Any = object()) -> None:
        expr = parse(json_path)
        result = expr.find(data)
        if result:
            if expect_value is object():
                return 
            assert result[0].value == expect_value, f'expect_value: {expect_value} not in data: {data}'
        else:
            raise AssertionError(f'json_path: {json_path} not in data: {data}')



def to_excel_data(data: list[dict]) -> bytes:
    """
    将列表转换为Excel文件数据
    """
    file = BytesIO()
    excel = ExcelWriter(file)
    excel.write(iter(data))
    excel.save()
    return file.getvalue()


class Data:
    base_path = Path(__file__).parent.parent / 'data'
    bootstrap = base_path / 'bootstrap.min.css'
    jquery = base_path / 'jquery.min.js'
    echarts = base_path / 'echarts.min.js'