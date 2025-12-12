from pydantic import BaseModel
import uuid
from fastapi_users import schemas

class PostCreate(BaseModel):
    title: str
    content: str

class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(UserRead):
    pass

class PostResponse(BaseModel):
    title: str
    content: str

class UpdatePost(BaseModel):
    title: str
    content: str
    id: int