#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/21 6:20 下午
import time
from datetime import timedelta, datetime
from typing import Generator, Optional, Union, Any
from fastapi import Header, Request, Depends
from sqlalchemy.orm import Session

from jose import jwt
from passlib.context import CryptContext
from pydantic import ValidationError

from commom import custom_exception
from commom.casbin import get_casbin
from core.config import settings
from db.session import SessionLocal
from server.auth_user import crud_user
from server.role_user import crud_role
from server.tenant import crud_tenant

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db() -> Generator:
    """
    获取sqlalchemy会话对象
    :return:
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def create_access_token(phone: str, expires_delta: timedelta = None) -> str:
    """
    生成token
    token里面的信息是对外公开的，所以可以根据生成token时传进来的手机号，对应返回

    :param phone: 用户手机号
    :param subject: 权限名称(可以换成权限层级ID)
    :param expires_delta: 时间
    :return:
    """

    if expires_delta:
        # expire = datetime.utcnow() + expires_delta
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    print(expire)
    to_encode = {"exp": expire, "phone": phone}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def jwt_authentication(
        request: Request,
        db: Session = Depends(get_db),
        token: str = Header(
            None, title="登陆Token",
            description="登陆、注册及开放的API不需要此参数")):
    """
    除了登陆、注册、文档不需要认证外，其他的都需要

    :param request:
    :param token:
    :return:
    """

    # 判断路由是否是文档、登陆、注册
    # 是：直接返回None
    # 否：接着往下走
    path_url = request.url.path.lower()
    if 'openapi' in path_url or 'login' in path_url or 'register' in path_url:
        return None

    # 判断token是否为空
    if not token:
        raise custom_exception.TokenAuthError()

    # 解析token
    try:
        jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise custom_exception.TokenExpired()
    except (jwt.JWTError, ValidationError, AttributeError):
        raise custom_exception.TokenAuthError()


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



def check_authority(
        request: Request,
        db: Session = Depends(get_db),
        token: Optional[str] = Depends(check_jwt_token)
):
    """
    权限校验 依赖于JWT token
    :param db:
    :param request:
    :param token:
    :return:
    """
    path_url = request.url.path.lower()
    if 'openapi' in path_url or 'login' in path_url or 'register' in path_url:
        return None

    user = crud_user.get_by_phone(db, phone=token.get("phone"))
    # if settings.SUPER_USER and sub == settings.SUPER_USER:
    #     return
    path = request.url.path
    method = request.method

    # 根据请求获取请求的路径和请求的方法，判断是否有权限
    e = get_casbin()
    role_info = crud_role.get(db, id=user.role_user_id)
    role_name = None
    if role_info:
        role_name = role_info.name
    tenant_info = crud_tenant.get(db, id=user.tenant_id)
    tenant_name = None
    if tenant_info:
        tenant_name = tenant_info.name
    if not e.enforce(role_name, tenant_name, path, method):
        # 判断不通过后说明没有该权限
        raise custom_exception.AuthenticationError()
    request.state.role = role_info
    request.state.user = user


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证密码
    :param plain_password: 原始密码
    :param hashed_password: hash后的密码
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    获取hash后的密码
    :param password:
    :return:
    """
    return pwd_context.hash(password)

