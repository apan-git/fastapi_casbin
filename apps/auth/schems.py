#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/25 5:44 下午


from pydantic import BaseModel


# 添加个人权限
class AuthCreateSingle(BaseModel):
    nickname: str
    parent_id: int
    path: str
    method: str


# 添加组权限
class AuthCreateGroup(BaseModel):
    username: str
    groupname: str
    path: str
    method: str
