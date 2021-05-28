#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/25 11:49 上午


from fastapi import APIRouter, Depends
from apps.auth.views import router as auth_router
from apps.user.views import router
from apps.user.views_test_api import router as test_router
from apps.resources.views import router as resource_router
from commom.deps import check_authority

api_router = APIRouter()

api_router.include_router(router, prefix="/user", tags=["用户操作"])
api_router.include_router(auth_router, prefix="/admin", tags=["权限操作"], dependencies=[Depends(check_authority)])
api_router.include_router(resource_router, prefix="/resource", tags=["资源操作"], dependencies=[Depends(check_authority)])
api_router.include_router(
    test_router,
    prefix="/test",
    dependencies=[Depends(check_authority)],
    tags=["测试权限接口"]
)


__all__ = ["api_router"]

