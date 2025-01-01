from itertools import cycle
import re
from typing import Any, Mapping, Self, Sequence, Union, get_origin, get_args, overload
from collections.abc import Iterable
import types


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs, readonly=False):
        # 收集类的注解和默认值
        annotations = {}
        defaults = {}
        
        # 从基类继承注解和默认值
        for base in bases:
            if hasattr(base, '__annotations__'):
                annotations.update(base.__annotations__)
            if hasattr(base, '__default__'):
                defaults.update(base.__default__)
        
        # 更新当前类的注解和默认值
        if '__annotations__' in attrs:
            annotations.update(attrs['__annotations__'])
        
        # 设置类属性
        attrs['__annotations__'] = annotations
        attrs['__annotations__'].pop('__show__', None)
        attrs['__default__'] = defaults
        attrs['__readonly__'] = readonly
        
        return super().__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    __show__: str | Sequence[str] | None = None

    @staticmethod
    def __init_value(cls_, value: Any):
        if cls_ is None:
            if isinstance(value, dict):
                return Model(value)
            elif isinstance(value, list):
                return [Model.__init_value(None, v) for v in value]
            elif isinstance(value, tuple):
                return tuple(Model.__init_value(None, v) for v in value)
            elif isinstance(value, set):
                return set(Model.__init_value(None, v) for v in value)
            else:
                return value
        if cls_ is dict:
            cls_ = Model
        try:
            if get_origin(cls_) is Union:
                return Model.__init_value(get_args(cls_)[0], value)
            elif type(cls_) is types.UnionType:
                args = getattr(cls_, '__args__', [])
                return Model.__init_value(args[0], value)
            elif type(cls_) is types.GenericAlias:
                origin = getattr(cls_, '__origin__', list)
                args = getattr(cls_, '__args__', [])
                if origin is dict:
                    return Model({Model.__init_value(args[0], k): Model.__init_value(args[1], v) for k, v in value.items()})
                else:
                    return origin((Model.__init_value(c, v) for c, v in zip(cycle(args), value)))
            else:
                return cls_(value)
        except:
            return value

    def __init__(self, __mapper: Mapping[str, Any] | None = None, **kwargs):
        super().__init__()
        readonly, self.__readonly__ = self.__readonly__, False
        
        # 直接保存所有字段，包括额外字段
        if __mapper:
            kwargs.update(__mapper)
        for key, value in kwargs.items():
            cls = self.__annotations__.get(key, None)
            self[key] = self.__init_value(cls, value)
            
        self.__readonly__ = readonly
    
    @classmethod
    def from_dict(cls, data: dict) -> Self:
        """将字典转换为模型对象"""
        if not isinstance(data, dict):
            raise ValueError(f"Expected dict, got {type(data)}")
            
        converted_data = {}
        for key, value in data.items():
            # 递归处理嵌套的数据结构
            if isinstance(value, dict):
                converted_data[key] = cls.from_dict(value)
            elif isinstance(value, list):
                converted_data[key] = cls.from_list(value)
            else:
                converted_data[key] = value
        return cls(**converted_data)
    
    @classmethod
    def from_list(cls, data: list[dict]) -> list[Self]:
        """将列表转换为模型对象列表"""
        if not isinstance(data, list):
            raise ValueError(f"Expected list, got {type(data)}")
            
        return [
            cls.from_dict(item) if isinstance(item, dict) else (cls.from_list(item) if isinstance(item, list) else item) for item in data
        ]  # type: ignore
    
    @classmethod
    @overload
    def from_object(cls, obj: dict) -> Self:
        ...
    @classmethod
    @overload
    def from_object(cls, obj: list[dict]) -> list[Self]:
        ...

    @classmethod
    @overload
    def from_object[T](cls, obj: T) -> T:
        ...
    

    @classmethod
    def from_object[V](cls, obj: dict[str, V] | list[V] | V):
        if isinstance(obj, dict):
            return cls.from_dict({k: cls.from_object(v) for k, v in obj.items()})
        elif isinstance(obj, Iterable):
            return [cls.from_object(item) for item in obj]
        else:
            return obj

    
    def __getattr__(self, key: str) -> Any:
        """支持通过属性方式访问字段"""
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")
    
    def __str__(self):
        show = self.__show__
        if not show:
            show = list(self.keys())  # 显示所有字段
        if isinstance(show, str):
            show = re.split(r'[,\s]+', show.strip())
        val = ', '.join(f"{key}={self[key]!r}" for key in show if key in self)
        return f'{self.__class__.__name__}({val})'

    __repr__ = __str__



if __name__ == "__main__":
    data = [{"id": "12321", "name": "abc"}]
    model = Model.from_list(data)
    print(model)
    print(model[0].id)
    print(model[0].name)
    # print(model.age)
    pass