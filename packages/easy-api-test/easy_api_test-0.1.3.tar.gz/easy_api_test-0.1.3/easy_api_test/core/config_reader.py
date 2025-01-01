
from os import PathLike
import os
import yaml

from .models import Model


class ConfigReader:
    def __init__(self, file_path: str | PathLike):
        self.file_path = file_path

    def read(self):
        pass

class YamlConfigReader(ConfigReader):
    def read(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)


class BaseSettings(Model):

    @classmethod
    def load_from_yaml_file(cls, file_path: str | PathLike):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'File not found: {file_path}')
        with open(file_path, 'r', encoding='utf-8') as f:
            return cls(**yaml.safe_load(f))
    
    @classmethod
    def load_from_data(cls, data: dict):
        return cls(**data)
