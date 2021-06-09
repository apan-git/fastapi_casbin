#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/28 10:01 上午


import random
from typing import Optional
from sqlalchemy.orm import Session

from apps.resources.models import TestResources
from db.crud_base import CRUDBase
from commom import deps

from apps.resources import schems


class CRUDResources(CRUDBase[
                       TestResources,
                       schems.CreateResources,
                       schems.UpdateResources]):
    @staticmethod
    def get_resources(db: Session, *, tenant_id: int, **kwargs) -> Optional[TestResources]:
        """
        通过手机号获取用户
        参数里面的* 表示 后面调用的时候 要用指定参数的方法调用
        正确调用方式
            curd_user.get_by_email(db, phone="xxx")
        错误调用方式
            curd_user.get_by_email(db, "xxx")
        :param tenant_id:
        :param db:
        :param phone:
        :return:
        """
        if tenant_id:
            obj = db.query(
                    TestResources
                ).filter(
                    TestResources.tenant_id == tenant_id
                ).filter_by(
                    **kwargs
                ).all()
        else:
            obj = db.query(
                TestResources
            ).filter_by(
                **kwargs
            ).all()

        return obj

    def create(self, db: Session, *, resources: schems.CreateResources, tenant_id: int = None) -> TestResources:
        db_obj = TestResources(
            name=resources.name,
            img=resources.img,
            doc=resources.doc,
            tenant_id=tenant_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


crud_resources = CRUDResources(TestResources)
