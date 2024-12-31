from easy_api_test.utils import AssertTools

def f():
    pass

def main():
    AssertTools.accept_error(f, not_contains_message='系统错误')


main()
print('ok')