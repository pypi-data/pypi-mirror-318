from pydantic import BaseModel
from datetime import datetime


class PromptSearchRequest(BaseModel):
    '''used for /search'''
    name: str
    org_id: int

class PromptRequest(BaseModel):
    '''used for /get and /delete'''
    id: int
    organization_id: int


class PromptBase(BaseModel):
    '''base class for prompt models'''
    name: str
    description: str
    content: str

class PromptCreateRequest(PromptBase):
    '''used for /create'''
    org_id: int


class PromptUpdateRequest(PromptBase):
    '''used for /update'''
    id: int

class Prompt(PromptBase):
    '''returned by all the api calls'''
    org_id: int
    id: int
    created_at: datetime
    updated_at: datetime
    version_id: int