from pydantic import BaseModel
from datetime import datetime

class FunctionSearchRequest(BaseModel):
    '''used for /search'''
    name: str
    org_id: int

class FunctionRequest(BaseModel):
    '''used for /get'''
    id: int
    org_id: int

class FunctionListAllRequest(BaseModel):
    '''used for /all'''
    org_id: int

class Function(BaseModel):
    id: int
    name: str
    description: str
    inputs: str
    outputs: str
    org_id: int
    created_at: datetime
    updated_at: datetime




