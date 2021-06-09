#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/22 5:32 下午
from typing import Optional

from pydantic import BaseModel, AnyHttpUrl

from db.base_class import get_uuid


class UserBase(BaseModel):
    phone: int


# 手机号登陆
class UserPhone(BaseModel):
    phone: int
    phone_code: int


class UserPassword(BaseModel):
    phone: int = None
    password: str = None


# 更新用户密码
class UserPasswordUpdate(UserPassword):
    new_password: str



# 创建账号
class UserCreate(UserBase):
    is_delete: Optional[bool] = False
    nick_name: str = None
    name: str
    password: str
    phone_code: int = 0
    tenant_id: int = None
    role_user_id: int = 1
    avatar: Optional[AnyHttpUrl] = None


# 更新账号
class UserUpdate(UserBase):
    phone_code: str = None
    password: str = None
    tenant_id: int = None
    trole_user_id: int = None
    avatar: Optional[AnyHttpUrl] = None


# 更新验证码
class UserUpdateCode(UserBase):
    phone_code: int


# 创建or获取验证码返回
class CreateUserResp(UserBase):
    pass
