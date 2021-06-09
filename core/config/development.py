# -*- coding: utf-8 -*-
"""
Date:2021/5/21 3:10 下午
"""

import os

from typing import Optional, Union

from pydantic import BaseSettings, AnyHttpUrl, IPvAnyAddress


class Settings(BaseSettings):
    # 开发模式配置
    DEBUG: bool = True

    # 项目文档
    TITLE: str = "FastAPI+MySQL+Tortoise-orm项目生成"
    DESCRIPTION: str = "FastAPI 基于 Tortoise-orm 实现的大型项目框架"
    # 文档地址 默认为docs
    DOCS_URL: str = "/openapi/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/openapi/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/openapi/re_doc"

    # token过期时间 分钟
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # 生成token的加密算法
    ALGORITHM: str = "HS256"

    # 生产环境保管好 SECRET_KEY
    SECRET_KEY: str = "aeq)s(*&(&)()WEQasd8**&^9asda_asdasd*&*&^+_sda"

    # 项目根路径
    BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))

    # RBAC 权限认证配置路径
    CASBIN_MODEL_PATH = os.path.join(BASE_PATH, 'core/config/rbac_model.conf')

    # 超级管理员
    SUPER_USER: str = 'super'

    # 异常请求返回码
    HTTP_418_EXCEPT = 418

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = "root"
    MYSQL_PASSWORD: str = "Apan123456.."
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = 'casbin_permission_db'

    # Mysql地址
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

    # redis地址
    REDIS_HOST:  Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    REDIS_PORT: int = 6379


settings = Settings()
