from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class AddressSchema(BaseModel):
    street: str = Field(..., min_length=3)
    city: str = Field(..., min_length=2)
    zip_code: str

class UserCreateSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    addresses: Optional[List[AddressSchema]] = []
