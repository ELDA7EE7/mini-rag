from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId
class Project(BaseModel):
    id: Optional[ObjectId] = Field(None, alias = "_id") #this type is weird for pydantic so we need to resolve it
    project_id: str = Field(...,min_length=1)

    #custom validation
    @field_validator('project_id')
    def validate_project_id(cls,value):
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        return value

    #this resolves the ObjectId pydantic problem
    class Config:
        arbitrary_types_allowed = True 