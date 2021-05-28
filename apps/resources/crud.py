#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/28 10:34 上午
from sqlalchemy.orm import Session

from server.resources import crud_resources
from .models import TestResources
from .schems import CreateResources, ReadResources


def add_res(resources: CreateResources, tenant_id, db: Session) -> TestResources:
    info = CreateResources(
        name=resources.name,
        img=resources.img,
        doc=resources.doc
    )
    obj = crud_resources.create(db, tenant_id=tenant_id, resources=info)
    return obj


def get_res(resources: ReadResources, tenant_id, db: Session):
    update_dict = resources.dict(exclude_unset=True)
    obj = crud_resources.get_resources(db, tenant_id=tenant_id, **update_dict)
    return obj

