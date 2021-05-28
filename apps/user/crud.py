#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/25 11:09 上午

"""
对角色数据库操作
"""
from typing import Union, Any

from sqlalchemy.orm import Session

from .models import AuthUser
from server.auth_user import crud_user
from .schems import UserCreate


async def get_user_by_phone(phone: int) -> Union[AuthUser, Any]:
    """
    :param phone:
    :return:
    """
    user = await crud_user.get_by_phone(phone=phone)
    return user


def add_user(db: Session, auth_user: UserCreate):
    phone_obj = db.query(AuthUser).filter(AuthUser.phone == auth_user.phone).first()
    if phone_obj:
        return None

    name_obj = db.query(AuthUser).filter(AuthUser.name == auth_user.name).first()
    if name_obj:
        return None

    auth_info = UserCreate(
        name=auth_user.name,
        nick_name=auth_user.nick_name,
        password=auth_user.password,
        phone=auth_user.phone,
        phone_code=auth_user.phone_code,
        avatar=auth_user.avatar,
        tenant_id=auth_user.tenant_id,
        role_user_id=auth_user.role_user_id
    )
    obj = crud_user.create(db, user=auth_info)
    return obj
