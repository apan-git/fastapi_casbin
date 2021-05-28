#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/28 9:53 上午
from pydantic import BaseModel


class Resources(BaseModel):
    name: str = None
    img: str = None
    doc: str = None


class CreateResources(Resources):
    pass


class UpdateResources(BaseModel):
    pass


class ReadResources(Resources):
    pass


class DelResources(BaseModel):
    id: int
    tenant_id: int



