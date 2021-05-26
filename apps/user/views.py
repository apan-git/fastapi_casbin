#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/24 10:31 上午
from datetime import timedelta
from typing import Any

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from apps.user.schems import CreateUserResp, UserCreate, UserPhone, UserPassword
from commom import deps
from commom.logger import logger
from commom.response_code import resp_200, resp_4003
from core.config import settings
from server.auth_user import crud_user

router = APIRouter()


# 获取验证码or创建用户
@router.post(
    "/register/",
    summary="获取验证码or创建用户",
    response_model=CreateUserResp
)
async def register(*, phone: int, password: str, db: Session = Depends(deps.get_db)) -> Any:
    user = crud_user.get_by_phone(db, phone=phone)
    if user:
        resp_user = crud_user.update_code(db, phone)
    else:
        user_info = UserCreate(phone=phone, password=password)
        resp_user = crud_user.create(db, user=user_info)
    return resp_200(data=resp_user.to_dict())


# 验证码登陆
@router.post('/login/', summary="验证码登陆")
async def login_access_token(*, db: Session = Depends(deps.get_db), user_info: UserPhone) -> Any:
    """
    用户通过验证码登陆换取token
    :param user_info: 用户手机号和验证码
    :param db:
    :return:
    """
    user = crud_user.authenticate(db, phone=user_info.phone, phone_code=user_info.phone_code)
    if not user:
        logger.info(f"验证码输入错误: code{user_info.phone_code}")
        return resp_4003(message="手机验证码输入有误")

    access_token_expires = timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = deps.create_access_token(phone=user.phone, expires_delta=access_token_expires)
    return resp_200(data={"token": token})


@router.post('/password/login/', summary="密码登陆")
async def login_access_token(*, db: Session = Depends(deps.get_db), user_info: UserPassword) -> Any:
    """
    用户通过手机号+密码换取token
    :param user_info: 用户手机号和密码
    :param db:
    :return:
    """
    phone = phone
    user = crud_user.authenticate(db, phone=user_info.phone, password=user_info.password)
    if not user:
        logger.info(f"密码输入错误: code{user_info.password}")
        return resp_4003(message="密码输入有误")

    access_token_expires = timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = deps.create_access_token(phone=user.phone, expires_delta=access_token_expires)
    return resp_200(data={"token": token})
