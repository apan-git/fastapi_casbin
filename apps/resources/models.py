#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/28 9:51 上午
from sqlalchemy import Column, VARCHAR, Integer, ForeignKey

from db.base_class import Base


class TestResources(Base):
    __tablename__ = "test_resources"
    name = Column(VARCHAR(255), nullable=False, comment="用户名")
    img = Column(VARCHAR(255), comment="图片")
    doc = Column(VARCHAR(255), comment="文案")
    tenant_id = Column(Integer, ForeignKey("tenant.id"), nullable=True,  comment="租户ID")
    __table_args__ = ({"comment": "测试资源表"})

    def to_dict(self):
        model_dict = dict(self.__dict__)
        del model_dict['_sa_instance_state']
        return model_dict




def init_db():
    from db.session import engine
    Base.metadata.create_all(engine)

# init_db()

