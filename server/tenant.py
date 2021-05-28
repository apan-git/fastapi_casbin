#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/27 10:43 上午

from sqlalchemy.orm import Session

from apps.user.models import Tenant
from db.crud_base import CRUDBase

from apps.auth import schems


class CRUDTenant(CRUDBase[Tenant, schems.TenantCreate, schems.TenantUpdate]):

    def create(self, db: Session, *, tenant: schems.TenantCreate) -> Tenant:
        db_obj = Tenant(
            name=tenant.name,
            doc=tenant.doc,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


crud_tenant = CRUDTenant(Tenant)
