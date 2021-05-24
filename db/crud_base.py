#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date:2021/5/22 5:16 下午
"""
CRUD基础类

"""
from typing import TypeVar, Generic, Type, Any, Optional, List, Union, Dict

from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType], db: Session):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        self.db = db

    def get(self, id: Any) -> Optional[ModelType]:
        return self.db.query(self.model).filter(self.model.id == id, self.model.is_delete == 0).first()

    # def get(self, id: Any) -> Optional[ModelType]:
    #     return selfdb.query(self.model).filter(self.model.id == id, self.model.is_delete == 0).first()

    # def get_multi(self, db: Session, *, page: int = 1, page_size: int = 100) -> List[ModelType]:
    #     temp_page = (page - 1) * page_size
    #     return db.query(self.model).filter(self.model.is_delete == 0).offset(temp_page).limit(page_size).all()

    def get_multi(self, *, page: int = 1, page_size: int = 100) -> List[ModelType]:
        temp_page = (page - 1) * page_size
        return self.db.query(self.model).filter(self.model.is_delete == 0).offset(temp_page).limit(page_size).all()

    # def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data)  # type: ignore
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    def create(self, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        self.db.add(db_obj)
        self.save(db_obj)
        return db_obj

    # def update(
    #         self,
    #         db: Session,
    #         *,
    #         db_obj: ModelType,
    #         obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    # ) -> ModelType:
    #     obj_data = jsonable_encoder(db_obj)
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     for field in obj_data:
    #         if field in update_data:
    #             setattr(db_obj, field, update_data[field])
    #     db.add(db_obj)
    #     self.save(dbdb_obj)
    #     return db_obj

    def update(self, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        self.save(db_obj)
        return db_obj

    def remove(self, id: int) -> ModelType:
        obj = self.db.query(self.model).filter(self.model.id == id).update({self.model.is_delete: 1})
        # db.delete(obj)
        self.db.commit()
        return obj

    def save(self, db_model):
        self.db.commit()
        self.db.flush()
        self.db.refresh(db_model)
        return db_model
