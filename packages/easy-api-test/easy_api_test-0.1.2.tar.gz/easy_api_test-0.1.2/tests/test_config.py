from easy_api_test import BaseSettings, Model

class Book(Model):
    name: str 
    author: str 
    price: int 

class Settings(BaseSettings):
    url: str 
    username: str 
    password: str 
    book: Book
    dog: Model



settings = Settings.load_from_yaml_file(r'.\tests\config.yaml') 

print(settings.url)
print(settings.username)
print(settings.book.name)
print(settings.book)
print(settings.dog.name)
