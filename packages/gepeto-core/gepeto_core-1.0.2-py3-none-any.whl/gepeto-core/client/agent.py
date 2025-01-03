from pydantic import BaseModel
from datetime import datetime
from typing import Union

from prompt import Prompt
from function import Function
from object import Object


class AgentSearchRequest(BaseModel):
    '''used for /search'''
    name: str

class AgentRequest(BaseModel):
    '''used for /get and /delete'''
    id: int

class AgentBase(BaseModel):
    '''base class for agent models'''
    name: str
    description: str = None
    model: str = "gpt-4o"
    instructions: str
    functions: list[Function]
    agent_transfers: list[int]
    tool_choice: str = "auto"  # Can be "none", "auto", or "required"
    parallel_tool_calls: bool = True
    max_tokens: int = 1000
    temperature: float = 0.0
    response_format: BaseModel = None

class AgentUpdateRequest(AgentBase):
    '''used for /update'''
    id: int
    prompt_id: int

class AgentCreateRequest(AgentBase):
    '''used for /create'''

class Agent(AgentBase):
    '''returned by all the api calls'''
    id: int
    prompt: Prompt
    created_at: datetime
    updated_at: datetime

    def equip(self, f: Union[Function, Object]) -> None:
        '''Add a function to this agent's capabilities'''
        pass

    def unequip(self, f: Union[Function, Object]) -> None:
        '''Remove a function from this agent's capabilities'''
        pass

    def response_format_to_json(self, model: BaseModel) -> dict:
        '''Convert response format model to JSON schema'''
        return model.model_json_schema()

    def json_to_response_format(self, schema: dict) -> BaseModel:
        '''Create response format model from JSON schema'''
        pass

    def function_to_json(self, f: Function) -> dict:
        '''Convert Function object to JSON representation'''
        pass

    def json_to_function(self, data: dict) -> Function:
        '''Create Function object from JSON data'''
        pass