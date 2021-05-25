#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/25 11:09 上午

"""
对角色数据库操作
"""
from typing import Union, Any
from .models import AuthUser
from server.auth_user import crud_user


async def get_user_by_phone(phone: int) -> Union[AuthUser, Any]:
    """
    :param phone:
    :return:
    """
    user = await crud_user.get_by_phone(phone=phone)
    return user