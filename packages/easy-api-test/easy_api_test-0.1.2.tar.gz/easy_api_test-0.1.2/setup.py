from setuptools import setup, find_packages

setup(
    name="easy_api_test",
    version="0.1.2",
    author="liulangjuanzhou",
    author_email="liulangjuanzhou@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "pytest>=6.0.0",
        "pyyaml>=5.4.0",
        "jsonpath_ng>=1.7.0",
        "lljz-tools>=0.3.4.3"
    ],
) 