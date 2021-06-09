#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/27 10:29 上午
from sqlalchemy.orm import Session

from apps.user.models import RoleUser
from db.crud_base import CRUDBase

from apps.auth import schems


class CRUDRoleUser(CRUDBase[RoleUser, schems.RoleUserCreate, schems.RoleUserUpdate]):

    def create(self, db: Session, *, role_user: schems.RoleUserCreate) -> RoleUser:
        db_obj = RoleUser(
            name=role_user.name,
            parent_id=role_user.parent_id,
            tenant_id=role_user.tenant_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


crud_role = CRUDRoleUser(RoleUser)

