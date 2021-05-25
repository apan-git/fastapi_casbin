#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/22 5:32 下午
from typing import Optional

from pydantic import BaseModel, AnyHttpUrl

from db.base_class import get_uuid


class UserBase(BaseModel):
    phone: int
    is_active: Optional[bool] = True


# 手机号登陆
class UserPhone(BaseModel):
    phone: int
    phone_code: int


# 创建账号
class UserCreate(UserBase):
    user_id: str = get_uuid()
    nickname: str = None
    password: str = None
    phone_code: int = 0
    permissions_id: int = 4
    parent_id: int = 1
    permission_merchants_id: int = 1
    avatar: Optional[AnyHttpUrl] = None
    email: str = None


# 更新账号
class UserUpdate(UserBase):
    phone_code: str
    password: str
    permissions_id: int
    parent_id: int
    avatar: Optional[AnyHttpUrl]


# 更新验证码
class UserUpdateCode(UserBase):
    phone_code: int


# 创建or获取验证码返回
class CreateUserResp(UserBase):
    pass
