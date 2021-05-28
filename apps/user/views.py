#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/24 10:31 上午
from datetime import timedelta
from typing import Any

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Request

from apps.user.crud import add_user
from apps.user.schems import UserCreate, UserPassword, UserUpdate, UserPasswordUpdate
from commom import deps
from commom.logger import logger
from commom.response_code import resp_200, resp_4003
from core.config import settings
from server.auth_user import crud_user

router = APIRouter()


# 创建用户
@router.post("/add/auth_user/register/", summary="创建用户or注册用户")
async def add_auth_user(request: Request, auth_user: UserCreate, db: Session = Depends(deps.get_db)):
    try:
        tenant_id = request.state.user.tenant_id
        if tenant_id:
            auth_user.tenant_id = tenant_id
    except Exception as error:
        print(error)
        pass
    user_obj = add_user(db=db, auth_user=auth_user)
    if user_obj:
        return resp_200(data={"auth_user": user_obj.to_dict()})
    else:
        return resp_200(code=201, message="用户名或手机号已存在")


# # 验证码登陆
# @router.post('/login/', summary="验证码登陆")
# async def login_access_token(*, db: Session = Depends(deps.get_db), user_info: UserPhone) -> Any:
#     """
#     用户通过验证码登陆换取token
#     :param user_info: 用户手机号和验证码
#     :param db:
#     :return:
#     """
#     user = crud_user.authenticate(db, phone=user_info.phone, phone_code=user_info.phone_code)
#     if not user:
#         logger.info(f"验证码输入错误: code{user_info.phone_code}")
#         return resp_4003(message="手机验证码输入有误")
#
#     access_token_expires = timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     token = deps.create_access_token(phone=user.phone, expires_delta=access_token_expires)
#     return resp_200(data={"token": token})


@router.post('/password/login/', summary="密码登陆")
async def login_access_token(*, db: Session = Depends(deps.get_db), user_info: UserPassword) -> Any:
    """
    用户通过手机号+密码换取token
    :param user_info: 用户手机号和密码
    :param db:
    :return:
    """
    user = crud_user.authenticate(db, phone=user_info.phone, password=user_info.password)
    if not user:
        logger.info(f"密码输入错误: code{user_info.password}")
        return resp_4003(message="密码输入有误")

    access_token_expires = timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = deps.create_access_token(phone=user.phone, expires_delta=access_token_expires)
    return resp_200(data={"token": token})


@router.post('/password/update/', name="密码修改")
async def login_access_token(*, db: Session = Depends(deps.get_db), user_info: UserPasswordUpdate) -> Any:
    """
    确保用户登陆或账号密码都输入正确
    :param user_info:
    :param db:
    :return:
    """

    user = crud_user.authenticate(db, phone=user_info.phone, password=user_info.password)
    if not user:
        logger.info(f"密码输入错误: code{user_info.password}")
        return resp_4003(message="密码输入有误")

    # 更新密码
    crud_user.update_password(db, phone=user_info.phone, new_password=user_info.new_password)
    access_token_expires = timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = deps.create_access_token(phone=user.phone, expires_delta=access_token_expires)
    return resp_200(data={"token": token})
