# -*- coding: utf-8 -*-
"""
@author: moxiaoying
@create: 2022/10/16
@description: 基础模型
"""
import asyncio
from datetime import datetime
from typing import Type

from tortoise import fields, Model
from pydantic import ConfigDict

from .utils import pydantic_model_creator


class BaseCrudMixin(Model):
    @classmethod
    async def create_one(cls, item: dict):
        return await cls.create(**item)

    @classmethod
    async def find_by(cls, **kwargs):
        return await cls.filter(**kwargs).all()

    @classmethod
    async def find_one(cls, **kwargs):
        return await cls.filter(**kwargs).first()

    @classmethod
    async def update_one(cls, _id: str, item: dict):
        update_obj = await cls.get_or_none(id=_id)
        if not update_obj:
            return
        await update_obj.update_from_dict(item).save()
        return update_obj

    @classmethod
    async def delete_one(cls, _id: str) -> int:
        deleted_count = await cls.filter(id=_id).delete()
        return deleted_count

    @classmethod
    async def delete_many(cls, ids: list) -> int:
        deleted_count = await cls.filter(id__in=ids).delete()
        return deleted_count


class BaseSchemaMixin:
    @classmethod
    def base_schema(cls: Type[Model], name, include=(), exclude=(), **kwargs):
        name = f'{cls.__name__}Schema{name}'
        optional = kwargs.pop('optional', ())
        # optional = kwargs.pop('optional', ()) or cls._meta.fields
        # print(f'{name}\t{optional}')
        # include = kwargs.get('include', ())
        if include:
            return pydantic_model_creator(cls, name=name, include=include, optional=optional,
                                          **kwargs)
        return pydantic_model_creator(cls, name=name, optional=optional, exclude=exclude,
                                      **kwargs)

    @classmethod
    def schema_list(cls, name='List', include=(), exclude=(), **kwargs):
        return cls.base_schema(name=name, include=include, exclude=exclude, **kwargs)

    @classmethod
    def schema_create(cls, name='Create', include=(), exclude=(), **kwargs):
        return cls.base_schema(name, include=include, exclude=exclude, exclude_readonly=True, **kwargs)

    @classmethod
    def schema_read(cls, name='Read', include=(), exclude=(), **kwargs):
        return cls.base_schema(name, include=include, exclude=exclude, **kwargs)

    @classmethod
    def schema_update(cls, name='Update', include=(), exclude=(), **kwargs):
        return cls.base_schema(name, include=include, exclude=exclude, exclude_readonly=True,
                               **kwargs)

    @classmethod
    def schema_filters(cls, name='Filters', include=(), exclude=(), **kwargs):
        return cls.base_schema(name, include=include, exclude=exclude, exclude_readonly=True,
                               **kwargs)

    @classmethod
    def schema_delete(cls):
        return int


class TimestampMixin:
    create_time = fields.DatetimeField(
        null=True, auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(
        null=True, auto_now=True, description="更新时间")


class BaseModel(BaseCrudMixin, BaseSchemaMixin, TimestampMixin):
    id = fields.IntField(pk=True, index=True, description="主键")
    status = fields.BooleanField(
        null=False, default=True, index=True, description="状态:True=启用,False=禁用")

    async def to_dict(self, m2m: bool = False, exclude_fields: list[str] | None = None):
        if exclude_fields is None:
            exclude_fields = []

        d = {}
        for field in self._meta.db_fields:
            if field not in exclude_fields:
                value = getattr(self, field)
                if isinstance(value, datetime):
                    value = value.strftime('%Y-%m-%d %H:%M:%S')
                d[field] = value
        if m2m:
            tasks = [self.__fetch_m2m_field(field) for field in self._meta.m2m_fields if field not in exclude_fields]
            results = await asyncio.gather(*tasks)
            for field, values in results:
                d[field] = values
        return d

    async def __fetch_m2m_field(self, field):
        values = [value for value in await getattr(self, field).all().values()]
        for value in values:
            value.update((k, v.strftime('%Y-%m-%d %H:%M:%S')) for k, v in value.items() if isinstance(v, datetime))
        return field, values

    class PydanticMeta:
        backward_relations = False
        model_config = ConfigDict(extra='ignore', strict=False)

    class Meta:
        abstract = True
        ordering = ['-update_time', '-create_time']


__all__ = [
    'BaseModel'
]
