from typing import Any, Dict
from pydantic import BaseModel


class UserFormModel(BaseModel):
    id: str
    login: str
    email: str
    fullName: str
    payload: Dict[str, Any]