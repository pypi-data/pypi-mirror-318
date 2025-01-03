from pydantic import BaseModel, field_validator, model_validator
from typing import List


class InitParamsValidator(BaseModel):
    username : str
    password : str
    env : str
    
    @field_validator('username', 'password', 'env')
    def check_str_input(cls, value, info):
        if not isinstance(value, str) or not value.strip():
           raise ValueError(f"O campo '{info.field_name}' deve ser strings e não {type(value)}")
        return value

class RequestValidator(BaseModel):
    url : str
    params : str
    timeout : int = 15

    @field_validator('url', 'params')
    def check_str_input(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O campo '{info.field_name}' deve ser uma string e não um {type(value)} e não vazio")
        return value
    
    @field_validator('timeout')
    def check_input_basic(cls, value, info):
        if not isinstance(value, int):
            raise ValueError(f"O campo '{info.field_name}' deve ser um inteiro e não um {type(value)}")
        
        return value

class PutValidator(BaseModel):
    url : str
    payload : dict
    timeout : int = 15

    @field_validator('url')
    def check_str_input(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O campo '{info.field_name}' deve ser uma string e não um {type(value)} e não vazio")
        return value
    
    @field_validator('timeout')
    def check_input_basic(cls, value, info):
        if not isinstance(value, int):
            raise ValueError(f"O campo '{info.field_name}' deve ser um inteiro e não um {type(value)}")
        return value
    
    @field_validator('payload')
    def check_dict_input(cls, value, info):
        if not isinstance(value, dict):
            raise ValueError(f"O campo '{info.field_name}' deve ser um dicionário e não um {type(value)}")
        return value

class PostValidator(BaseModel):
    url : str
    variables : dict

    @field_validator('url')
    def check_str_input(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O campo '{info.field_name}' deve ser uma string e não um {type(value)} e não vazio")
        return value
    
    @field_validator('variables')
    def check_dict_input(cls, value, info):
        if not isinstance(value, dict):
            raise ValueError(f"O campo '{info.field_name}' deve ser um dicionário e não um {type(value)}")
        return value

class ListTicketValidator(BaseModel):
    tabela : str
    query : str
    campos : List[str]
    timeout : int
    limit : int
    
    @field_validator('tabela', 'query')
    def check_str_input(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O campo '{info.field_name}' deve ser uma string e não um {type(value)} e não vazio")
        return value
    
    @field_validator('timeout', 'limit')
    def check_input_basic(cls, value, info):
        if not isinstance(value, int):
            raise ValueError(f"O campo '{info.field_name}' deve ser um inteiro e não um {type(value)}")
        return value
    
    @field_validator('campos')
    def check_list_input(cls, value, info):
        if not isinstance(value, list):
            raise ValueError(f"O campo '{info.field_name}' deve ser uma lista e não um {type(value)}")
        return value
    
class UpdateTicketValidator(BaseModel):
    sys_id : str
    tabela : str
    payload : List[str]
    timeout : int

    @field_validator('sys_id', 'tabela')
    def check_str_input(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O campo '{info.field_name}' deve ser uma string e não um {type(value)} e não vazio")
        return value
    
    @field_validator('timeout')
    def check_input_basic(cls, value, info):
        if not isinstance(value, int):
            raise ValueError(f"O campo '{info.field_name}' deve ser um inteiro e não um {type(value)}")
        return value

    @field_validator('payload')
    def check_list_input(cls, value, info):
        if not isinstance(value, list):
            raise ValueError(f"O campo '{info.field_name}' deve ser uma lista e não um {type(value)}")
        return value

class AttachFileTicketValidator(BaseModel):
    header_content_type : dict
    anexo_path : str
    tabela : str
    sys_id : str
    timeout : int

    @field_validator('sys_id', 'tabela', 'anexo_path')
    def check_str_input(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O campo '{info.field_name}' deve ser uma string e não um {type(value)} e não vazio")
        return value
    
    @field_validator('timeout')
    def check_input_basic(cls, value, info):
        if not isinstance(value, int):
            raise ValueError(f"O campo '{info.field_name}' deve ser um inteiro e não um {type(value)}")
        return value
    
    @field_validator('header_content_type')
    def check_dict_input(cls, value, info):
        if not isinstance(value, dict):
            raise ValueError(f"O campo '{info.field_name}' deve ser um dicionário e não um {type(value)}")
        return value
    
class GetAttachValidator(BaseModel):
    sys_id : str
    tabela : str
    campo :str
    download_dir : str
    timeout : int

    @field_validator('sys_id', 'tabela', 'campo', 'download_dir')
    def check_str_input(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O campo '{info.field_name}' deve ser uma string e não um {type(value)} e não vazio")
        return value
    
    @field_validator('timeout')
    def check_input_basic(cls, value, info):
        if not isinstance(value, int):
            raise ValueError(f"O campo '{info.field_name}' deve ser um inteiro e não um {type(value)}")
        return value