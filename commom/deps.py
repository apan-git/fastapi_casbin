#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/21 6:20 下午
from typing import Generator, Optional, Union, Any

from fastapi import Header
from jose import jwt
from pydantic import ValidationError

from commom import custom_exception
from core.config import settings
from db.session import SessionLocal


def get_db() -> Generator:
    """
    获取sqlalchemy会话对象
    :return:
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.clone()


def check_jwt_token(
        token: Optional[str] = Header(..., description="登陆token")) -> Union[str, Any]:
    """
    解析token 默认headers里面为token字段的数据
    可以给headers里面的token换名字例如 X-token
    :param token:
    :return:
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise custom_exception.TokenExpired()
    except (jwt.JWTError, ValidationError, AttributeError):
        raise custom_exception.TokenAuthError()