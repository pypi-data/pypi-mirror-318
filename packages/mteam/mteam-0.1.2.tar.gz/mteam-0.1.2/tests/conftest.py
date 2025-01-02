import pytest
from dotenv import load_dotenv

# 在所有测试开始前加载环境变量
def pytest_configure(config):
    load_dotenv() 