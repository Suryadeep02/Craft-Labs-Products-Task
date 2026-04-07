from pydantic import BaseModel

#Pydantic Models to create

class Product(BaseModel):
    id: int
    name: str 
    description: str 
    price: float