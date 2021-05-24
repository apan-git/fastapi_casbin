#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/22 5:32 下午
from typing import Optional

from pydantic import BaseModel, EmailStr, AnyHttpUrl


class UserBase(BaseModel):
    # email: Optional[EmailStr] = None
    phone: int = None
    is_active: Optional[bool] = True


# 手机号登陆
class UserPhone(UserBase):
    phone_code: int


# 创建账号
class UserCreate(UserBase):
    nickname: str = None
    password: str = None
    phone_code: int
    permissions_id: int = None
    parent_id: int = 0
    avatar: Optional[AnyHttpUrl] = None


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
