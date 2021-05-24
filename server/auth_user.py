#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/22 5:28 下午
import random
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

    def create(self, db: Session, *, user: request_schems.UserCreate) -> AuthUser:
        phone_code = self.phone_send_code(user.phone)
        user_exists = self.get_by_phone(db, phone=user.phone)
        if user_exists:
            raise Exception(f"{user.phone}该用户已存在")
        db_obj = AuthUser(
            phone=user.phone,
            phone_code=phone_code,
            parent_id=user.parent_id,
            avatar=user.avatar,
            password=user.password,
            nickname=user.nickname
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, phone, obj_in: request_schems.UserUpdate) -> AuthUser:
        db_user = self.get_by_phone(db, phone=phone)
        if db_user:
            update_dict = obj_in.dict(exclude_unset=True)
            for k, v in update_dict.items():
                setattr(db_user, k, v)
            db.commit()
            db.flush()
            db.refresh(db_user)
            return db_user

    def update_code(self, db: Session, phone) -> AuthUser:
        db_user = self.get_by_phone(db, phone=phone)
        if db_user:
            code = self.phone_send_code(phone)
            setattr(db_user, "phone_code", code)
            db.commit()
            db.flush()
            db.refresh(db_user)
            return db_user

    @staticmethod
    def phone_send_code(phone):
        sms_head = "【测试验证码】"
        code = ""
        for i in range(0, 6):
            st1 = str(random.randint(0, 9))
            code += st1
        sms_context = f"{sms_head}本次验证码为:{code}, 有效期为3分钟"
        a1 = f"发送手机号为{phone}"
        print(a1, sms_context)
        return code

    def authenticate(self, db: Session, *, phone: int, phone_code: str) -> Optional[AuthUser]:
        user = self.get_by_phone(db, phone=phone)
        if not user:
            return None
        if user.phone_code != phone_code:
            return None
        return user

curd_user = CRUDAuthUser(AuthUser)