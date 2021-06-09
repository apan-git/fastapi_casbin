#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/27 10:56 上午
from sqlalchemy.orm import Session

from apps.auth.schems import TenantCreate, RoleUserCreate
from apps.user.models import Tenant, RoleUser
from server.role_user import crud_role
from server.tenant import crud_tenant


def create_tenant(db: Session, tenant: TenantCreate):
    tenant_name = db.query(Tenant).filter(Tenant.name == tenant.name).first()
    if tenant_name:
        return None
    tenant_info = TenantCreate(
        name=tenant.name,
        doc=tenant.doc,
    )
    obj = crud_tenant.create(db, tenant=tenant_info)
    return obj


def create_role(db: Session, role: RoleUserCreate):
    role_name = db.query(RoleUser).filter(RoleUser.name == role.name).first()
    if role_name:
        return None
    role_info = RoleUserCreate(
        name=role.name,
        parent_id=role.parent_id,
        tenant_id=role.tenant_id
    )
    obj = crud_role.create(db, role_user=role_info)
    return obj
