#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/25 5:44 下午


from pydantic import BaseModel


# 添加个人权限
class AuthCreateSingle(BaseModel):
    role_name: str
    tenant_name: str
    path: str
    method: str
    exists: int


# 添加组权限
class AuthCreateGroup(BaseModel):
    username: str
    groupname: str


# 创建角色
class RoleUserCreate(BaseModel):
    name: str
    parent_id: int = None
    tenant_id: int = None


# 创建角色
class RoleUserUpdate(BaseModel):
    parent_id: int
    tenant_id: int


# 创建租户
class TenantCreate(BaseModel):
    name: str
    doc: str


# 修改租户
class TenantUpdate(BaseModel):
    doc: str
