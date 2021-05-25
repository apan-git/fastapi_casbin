#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/25 4:43 下午
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from commom.response_code import resp_200
from commom import deps

router = APIRouter()


# 测试接口1
@router.post("/test1/", summary="测试接口1")
async def test1(request: Request, *, db: Session = Depends(deps.get_db)):
    print(request.state.user.to_dict())
    return resp_200()


# 测试接口1
@router.post("/test2/", summary="测试接口2")
async def test1(request: Request, *, db: Session = Depends(deps.get_db)):
    print(request.state.user.to_dict())
    return resp_200()


# 测试接口1
@router.post("/test3/", summary="测试接口3")
async def test1(request: Request, *, db: Session = Depends(deps.get_db)):
    print(request.state.user.to_dict())
    return resp_200()


# 测试接口1
@router.post("/test4/", summary="测试接口4")
async def test1(request: Request, *, db: Session = Depends(deps.get_db)):
    print(request.state.user.to_dict())
    return resp_200()


# 测试接口1
@router.post("/test5/", summary="测试接口5")
async def test1(request: Request, *, db: Session = Depends(deps.get_db)):
    print(request.state.user.to_dict())
    return resp_200()


# 测试接口1
@router.post("/test6/", summary="测试接口6")
async def test1(request: Request, *, db: Session = Depends(deps.get_db)):
    print(request.state.user.to_dict())
    return resp_200()


# 测试接口1
@router.post("/test7/", summary="测试接口7")
async def test1(request: Request, *, db: Session = Depends(deps.get_db)):
    print(request.state.user.to_dict())
    return resp_200()
