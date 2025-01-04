import os
import pytest
from dotenv import load_dotenv

def pytest_configure(config):
    """设置测试环境"""
    # 加载环境变量
    load_dotenv()

    # 确保必要的环境变量存在
    required_vars = ['app_id', 'app_secret', 'app_token']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        pytest.exit(f"Missing required environment variables: {', '.join(missing_vars)}") 