#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/28 10:28 上午


from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from apps.resources.crud import add_res, get_res
from apps.resources.schems import CreateResources, ReadResources
from commom.deps import get_db
from commom.response_code import resp_200

router = APIRouter()


@router.post("/add/resources/", name="添加资源")
async def add_resources(request: Request, resource: CreateResources, db: Session = Depends(get_db)):
    tenant_id = request.state.role.tenant_id
    data = add_res(resources=resource, tenant_id=tenant_id, db=db).to_dict()
    return resp_200(data={"data": data})


@router.post("/get/resources/", name="查看资源")
async def get_resources(request: Request, resource: ReadResources, db: Session = Depends(get_db)):
    tenant_id = request.state.role.tenant_id
    data = get_res(resources=resource, tenant_id=tenant_id, db=db)
    return resp_200(data={"data": data})
