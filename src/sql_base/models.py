from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class cafe(BaseModel):
    id: Optional[int]
    city: str
    number: int
    name: str
    address: str
    Menu_ID: int
    Staff_ID: int
class menu(BaseModel):
    id: Optional[int]
    price: int
    weight: int
    ingredient: str
    availability: str
    name_of_the_dish_ID: int

class staff(BaseModel):
    id: Optional[int]
    name: str
    surname: str
    Patronymic: int
    datee: int
    cafe: str
    Post_ID: int


class User(BaseModel):
    login: str
    password: str
    post: Optional[int]
    reg_date: Optional[datetime]






