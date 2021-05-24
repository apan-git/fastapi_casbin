# -*- coding: utf-8 -*-
"""
Date:2021/5/21 3:01 下午
"""

"""
待处理，实现多租户权限，
优先处理，账号创建等权限处理

"""


import uvicorn

from core.server import create_app

api_router = create_app()

if __name__ == '__main__':
    uvicorn.run(api_router)
