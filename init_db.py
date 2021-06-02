#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/31 4:29 下午
from sqlalchemy.orm import Session

from apps.auth.schems import RoleUserCreate
from apps.user.schems import UserCreate
from db.session import SessionLocal
from commom.deps import crud_user, crud_role

role_user = [{"name": "超级管理员"}, {"name": "普通角色", "parent_id": 1}]

auth_user = [
    {
        "name": "admin", "nick_name": "admin", "password": "123456",
        "phone": "11111111111", "role_user_id": 1
    },
    {
        "name": "test", "nick_name": "test", "password": "123456",
        "phone": "22222222222", "role_user_id": 2
    },
]


def create_super_user(db: Session) -> None:
    for role in role_user:
        role_info = RoleUserCreate(
            name=role.get("name"),
            parent_id=role.get("parent_id", None)
        )
        role_obj = crud_role.create(db, role_user=role_info)
        print(role_obj.to_dict())
    for auth in auth_user:
        auth_info = UserCreate(
            name=auth.get("name"),
            nick_name=auth.get("nick_name"),
            phone=auth.get("phone"),
            password=auth.get("password"),
            role_user_id=auth.get("role_user_id"),
            is_delete=False,
            phone_code=0,
            avatar=None,
        )
        user_obj = crud_user.create(db, user=auth_info)
        print(user_obj.to_dict())


if __name__ == '__main__':
    db = SessionLocal()
    create_super_user(db)
