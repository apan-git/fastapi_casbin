#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/22 5:28 下午
from typing import Optional

from sqlalchemy.orm import Session

from apps.user.models import AuthUser
from db.crud_base import CRUDBase

from apps.user import request_schems


class CRUDAuthUser(CRUDBase[
                       AuthUser,
                       request_schems.UserCreate,
                       request_schems.UserPhone]):
    @staticmethod
    def get_by_phone(db: Session, *, phone: int) -> Optional[AuthUser]:
        """
        通过手机号获取用户
        参数里面的* 表示 后面调用的时候 要用指定参数的方法调用
        正确调用方式
            curd_user.get_by_email(db, email="xxx")
        错误调用方式
            curd_user.get_by_email(db, "xxx")
        :param db:
        :param phone:
        :return:
        """
        return db.query(AuthUser).filter(AuthUser.phone == phone).first()

    def create(self, db: Session, *, obj_in: request_schems.UserCreate) -> SysUser:
        phone_code = ""
        db_obj = AuthUser(
            phone=obj_in.phone,
            phone_code=phone_code,
            parent_id=obj_in.parent_id,
            avatar=obj_in.avatar,
            password=obj_in.password,
            nickname=obj_in.nickname
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def phone_send_code(phone):
        code = ""
        return code
