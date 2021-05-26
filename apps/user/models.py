#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/22 3:09 下午


from sqlalchemy import Column, Integer, VARCHAR, BigInteger
from db.base import Base


class Tenant(Base):
    """
    商户表
    """
    __tablename__ = "tenant"
    name = Column(VARCHAR(128), unique=True, comment="租户名")
    doc = Column(VARCHAR(255), comment="介绍")

    __table_args__ = ({"comment": "租户"})


class RoleUser(Base):
    __tablename__ = "role_user"
    name = Column(VARCHAR(255), unique=True, comment="角色名")
    parent_id = Column(Integer, default=0, comment="父级角色")
    tenant_id = Column(Integer, default=0, comment="租户ID")
    __table_args__ = ({"comment": "角色"})


class AuthUser(Base):
    __tablename__ = "auth_user"
    name = Column(VARCHAR(255), unique=True, comment="用户名")
    nick_name = Column(VARCHAR(255), comment="昵称")
    password = Column(VARCHAR(255), comment="密码")
    phone = Column(BigInteger, comment="手机号")
    phone_code = Column(Integer, default=0, comment="手机验证码")
    avatar = Column(VARCHAR(256), comment="头像")
    tenant_id = Column(Integer, default=0, comment="租户ID")
    __table_args__ = ({"comment": "用户"})


# class Permission(Base):
#     __tablename__ = 'permission'
#     permissions_name = Column(VARCHAR(128), default="管理员", comment="权限级别")
#
#     __table_args__ = ({'comment': '权限等级'})


# class AuthUser(Base):
#     """
#     用户表
#     """
#     __tablename__ = "auth_user"
#     user_id = Column(VARCHAR(32), default=get_uuid(), unique=True, comment="用户的ID")
#     phone = Column(BigInteger, unique=True, index=True, nullable=False, comment="手机号")
#     phone_code = Column(Integer, nullable=False, comment="手机验证码")
#     email = Column(VARCHAR(128), index=True, default="", comment="邮箱")
#     nickname = Column(VARCHAR(128), comment="管理员昵称")
#     avatar = Column(VARCHAR(256), comment="管理员头像")
#     password = Column(VARCHAR(128), comment="密码")
#     permissions_id = Column(Integer, nullable=True)
#     permission_merchants_id = Column(Integer, comment="租户ID")
#     parent_id = Column(Integer, default=0, comment="父角色ID")
#     __table_args__ = ({"comment": "权限角色表"})
#
#     def to_dict(self):
#         model_dict = dict(self.__dict__)
#         del model_dict['_sa_instance_state']
#         return model_dict
#
#
# class PermissionMerchants(Base):
#     """
#     商户表
#     """
#     __tablename__ = "permission_merchants"
#     name = Column(VARCHAR(128), unique=True, comment="租户名")
#     doc = Column(VARCHAR(255), comment="介绍")
#
#     __table_args__ = ({"comment": "租户表"})


def init_db():
    from db.session import engine
    Base.metadata.create_all(engine)

# init_db()
