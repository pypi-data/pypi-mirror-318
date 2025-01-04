
import json
import yaml
import tomllib
import configparser
from os import PathLike
from pathlib import Path

from lljz_tools import Model


class ConfigReader:
    def __init__(self, file_path: str | PathLike):
        self.file_path = file_path

    def read(self):
        pass

class YamlConfigReader(ConfigReader):
    def read(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)


class BaseSettings(Model, readonly=True):

    @classmethod
    def load_from_file(cls, file_path: str | PathLike, suffix: str = ''):

        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f'File not found: {file_path}')
        suffix = (suffix or path.suffix).lower()
        if path.suffix == '.yaml':
            return cls.load_from_yaml_file(file_path)
        elif path.suffix == '.toml':
            return cls.load_from_toml_file(file_path)
        elif path.suffix == '.json':
            return cls.load_from_json_file(file_path)
        else:
            raise ValueError(f'Unsupported file type: {path.suffix}')

    @classmethod
    def load_from_ini_file(cls, file_path: str | PathLike):
        config = configparser.ConfigParser()
        config.read(file_path)
        result_dict = {}
        for section in config.sections():
            result_dict[section] = {}
            for key, value in config.items(section):
                result_dict[section][key] = value
        return cls(result_dict)

    @classmethod
    def load_from_json_file(cls, file_path: str | PathLike):
        with open(file_path, 'r', encoding='utf-8') as f:
            return cls(json.load(f))


    @classmethod
    def load_from_yaml_file(cls, file_path: str | PathLike):
        with open(file_path, 'r', encoding='utf-8') as f:
            return cls(yaml.safe_load(f))
    
    @classmethod
    def load_from_toml_file(cls, file_path: str | PathLike):
        with open(file_path, 'rb') as f:
            return cls(tomllib.load(f))

    @classmethod
    def load_from_data(cls, data: dict):
        return cls(data)


if __name__ == '__main__':
    print(BaseSettings.load_from_ini_file('./data/config.ini'))
