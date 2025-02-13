from pydantic import BaseModel


class Soma(BaseModel):
    number1: int
    number2: int