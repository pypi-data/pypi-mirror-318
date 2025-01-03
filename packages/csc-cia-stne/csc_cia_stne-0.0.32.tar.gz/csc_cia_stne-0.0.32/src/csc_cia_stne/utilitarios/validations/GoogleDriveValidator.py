
from pydantic import BaseModel, field_validator
class InitParamsValidator(BaseModel):
    key: str
    with_subject: str
    scopes : list
    version : str

    @field_validator('key','with_subject', "version")
    def check_str_input(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O campo '{info.field_name}' deve ser strings e não {type(value)}")
        return value
    @field_validator('scopes')
    def check_list_input(cls, value, info):
        if not isinstance(value, list):
            raise ValueError(f"O parametro '{info.field_name}' deve ser uma lista")
        
        return value

class CreateFolderValidator(BaseModel):
    name: str
    parent_folder_id: str

    @field_validator('name','parent_folder_id')
    def check_str_input(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O campo '{info.field_name}' deve ser strings e não {type(value)}")
        return value

class ListFolderValidator(BaseModel):
    query : str
    spaces: str
    fields : str
    @field_validator('query','spaces','fields')
    def check_str_input(cls, value, info):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"O campo '{info.field_name}' deve ser strings e não {type(value)}")
        return value