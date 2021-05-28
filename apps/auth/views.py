#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/25 5:41 下午
from typing import List

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from apps.auth.crud import create_tenant, create_role
from apps.auth.schems import AuthCreateSingle, AuthCreateGroup, TenantCreate, RoleUserCreate
from commom.casbin import get_casbin
from commom.response_code import resp_200, resp_4001
from commom import deps

router = APIRouter()


@router.post("/add/tenant/", summary="添加租户", name="添加租户", description="添加租户")
async def add_tenant(tenant: TenantCreate, db: Session = Depends(deps.get_db)):
    tenant_obj = create_tenant(db=db, tenant=tenant)
    if tenant_obj:
        return resp_200(data={"tenant": tenant_obj.to_dict()})
    else:
        return resp_200(code=201, message="租户名称已存在")


@router.post("/add/role/", summary="添加角色", name="添加角色", description="添加角色")
async def add_role(request: Request, role: RoleUserCreate, db: Session = Depends(deps.get_db)):
    if request.state.role.name != "超级管理员":
        role.parent_id = request.state.role.id
        role.tenant_id = request.state.role.tenant_id
    role_obj = create_role(db=db, role=role)
    if role_obj:
        return resp_200(data={"tenant": role_obj.to_dict()})
    else:
        return resp_200(code=201, message="角色名称已存在")


# 添加个人访问权限
@router.post("/add/auth/", summary="添加访问权限", name="添加访问权限", description="添加访问权限")
async def add_single_auth(authority_list: List[AuthCreateSingle]):
    e = get_casbin()
    for authority_info in authority_list:
        policy = (authority_info.role_name, authority_info.tenant_name, authority_info.path, authority_info.method)
        has_policy = e.has_policy(*policy)
        if has_policy and authority_info.exists == 0:
            e.remove_policy(*policy)
        elif not has_policy and authority_info.exists == 1:
            res = e.add_policy(
                authority_info.role_name,
                authority_info.tenant_name,
                authority_info.path,
                authority_info.method
            )
    return resp_200()


# 添加组权限
@router.post("/add/group_auth/", summary="添加组访问权限", name="添加组访问权限", description="添加组访问权限")
async def add_single_auth(authority_info: AuthCreateGroup):
    e = get_casbin()
    res = e.add_grouping_policy(
        authority_info.username,
        authority_info.groupname,
    )
    if res:
        return resp_200()
    else:
        return resp_4001(message="添加权限失败")


# 查看当前角色权限
@router.post("/add/group_auth/", summary="查看当前角色权限", name="查看当前角色权限", description="查看当前角色权限")
async def get_role_permissions(request: Request):
    e = get_casbin()
    role_name = request.state.role.name
    res = e.add_policy(
        role_name
    )
    return resp_200()
