# -*- coding: utf-8 -*-
"""
Date:2021/5/21 3:01 下午
"""
import uvicorn

from core.server import create_app

api_router = create_app()

if __name__ == '__main__':
    uvicorn.run(api_router)
