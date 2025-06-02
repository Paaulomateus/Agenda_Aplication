from typing import List
from pydantic import BaseModel
from fastapi import HTTPException

# MODELS
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int = None

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

# Simulação de banco de dados em memória
users_db: List[User] = []
products_db: List[Product] = []

# CLASSES CRUD PARA PRODUCT
class ProductCreateView:
    def create(self, product: Product) -> Product:
        products_db.append(product)
        return product

class ProductEditView:
    def edit(self, product_id: int, product: Product) -> Product:
        for idx, prod in enumerate(products_db):
            if prod.id == product_id:
                products_db[idx] = product
                return product
        raise HTTPException(status_code=404, detail="Produto não encontrado")

class ProductDetailView:
    def detail(self, product_id: int) -> Product:
        for prod in products_db:
            if prod.id == product_id:
                return prod
        raise HTTPException(status_code=404, detail="Produto não encontrado")

class ProductListView:
    def list(self) -> List[Product]:
        return products_db

class ProductDeleteView:
    def delete(self, product_id: int) -> dict:
        for idx, prod in enumerate(products_db):
            if prod.id == product_id:
                del products_db[idx]
                return {"message": "Produto deletado"}
        raise HTTPException(status_code=404, detail="Produto não encontrado")

# MÉTODOS CRUD PARA USER

def user_create(user: User) -> User:
    users_db.append(user)
    return user

def user_edit(user_id: int, user: User) -> User:
    for idx, u in enumerate(users_db):
        if u.id == user_id:
            users_db[idx] = user
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

def user_detail(user_id: int) -> User:
    for u in users_db:
        if u.id == user_id:
            return u
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

def user_list() -> List[User]:
    return users_db

def user_delete(user_id: int) -> dict:
    for idx, u in enumerate(users_db):
        if u.id == user_id:
            del users_db[idx]
            return {"message": "Usuário deletado"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
