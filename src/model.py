from typing import Dict
from pydantic import BaseModel
from datetime import datetime

# Класс, который описывает структуру ответа сервера для метода,
# который подсчитывает символы в строке.
# Данный класс обязательно должен быть наследован от pydantic.BaseModel!

class GetInfoNote(BaseModel):
    created_at: datetime
    updated_at: datetime

class GetTextNote(BaseModel):
    id: int
    text: str

class PostNote(BaseModel):
    id: int

class GetListNote(BaseModel):
    notes: Dict[int, int]

