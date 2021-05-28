#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/25 2:32 下午

import casbin
import casbin_sqlalchemy_adapter
from db.session import engine
from core.config import settings


def get_casbin() -> casbin.Enforcer:
    adapter = casbin_sqlalchemy_adapter.Adapter(engine)
    e = casbin.Enforcer(settings.CASBIN_MODEL_PATH, adapter)
    return e
