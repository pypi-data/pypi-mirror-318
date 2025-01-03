from pydantic import BaseModel
from function import Function
from datetime import datetime

class ObjectBase(BaseModel):
    '''base class for object models'''
    org_id: int

class ObjectSearchRequest(ObjectBase):
    '''used for /search'''
    name: str

class ObjectRequest(ObjectBase):
    '''used for /get'''
    id: int

class ObjectListAllRequest(ObjectBase):
    '''used for /all'''
    pass

class Object(BaseModel):
    id: int
    name: str
    description: str
    methods: list[Function]
    org_id: int
    created_at: datetime
    updated_at: datetime