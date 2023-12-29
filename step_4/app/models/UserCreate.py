from pydantic import BaseModel, PositiveInt, Field

class UserCreate(BaseModel):
    name: str
    email: str
    age: PositiveInt | None = Field(default=None, lt=130)
    is_subscribed: bool
