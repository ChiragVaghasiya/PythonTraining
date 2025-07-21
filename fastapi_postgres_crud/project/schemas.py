from pydantic import BaseModel, EmailStr


class ProductBase(BaseModel):
    name: str
    price: float


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class CustomerBase(BaseModel):
    name: str
    email: EmailStr


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True
