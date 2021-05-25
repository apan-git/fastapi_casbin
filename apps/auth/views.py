#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/25 5:41 下午

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from apps.auth.schems import AuthCreateSingle, AuthCreateGroup
from commom.casbin import get_casbin
from commom.response_code import resp_200, resp_4001
from commom import deps

router = APIRouter()


# 添加个人访问权限
@router.post("/add/auth/", summary="添加访问权限", name="添加访问权限", description="添加访问权限")
async def add_single_auth(authority_info: AuthCreateSingle):
    e = get_casbin()
    res = e.add_policy(
        authority_info.nickname,
        authority_info.parent_id,
        authority_info.path,
        authority_info.method
    )
    if res:
        return resp_200()
    else:
        return resp_4001(message="添加权限失败")


# 添加组权限
@router.post("/add/group_auth/", summary="添加组访问权限", name="添加组访问权限", description="添加组访问权限")
async def add_single_auth(authority_info: AuthCreateGroup):
    e = get_casbin()
    res = e.add_grouping_policy(
        authority_info.username,
        authority_info.groupname,
        authority_info.path,
        authority_info.method
    )
    if res:
        return resp_200()
    else:
        return resp_4001(message="添加权限失败")

# e = get_casbin()
# res = e.add_grouping_policy("xiaoapan", "apan", "kaifabu")
# print(res)