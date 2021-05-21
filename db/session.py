#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/21 6:03 下午


"""
create_engine 传入两个参数，一个是刚才上面创建的 database uri ，
一个是一个pool_pre_ping （是否预加载连接池），

再创建一个 SessionLocal，这里的Session 指的是 Data Session。
autocommit ： 是否自动提交

autoflush：是否自动刷新并加载数据库

bind ：绑定数据库引擎

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
