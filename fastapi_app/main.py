from fastapi import FastAPI, Path, Query, APIRouter, HTTPException
from enum import Enum
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Pydantic Data Models
class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

# Simulação de banco em memória
users_db: List[User] = []
products_db: List[Product] = []

# Enum for Path Parameter
class ColorEnum(str, Enum):
    red = "red"
    green = "green"
    blue = "blue"

# 1. Endpoint com Path Parameter
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# 2. Endpoint com Path Parameter com Enum
@app.get("/color/{color}")
def get_color(color: ColorEnum):
    return {"color": color}

# 3. Endpoint com Path Parameter com Path (validação extra)
@app.get("/product/{product_id}")
def get_product(product_id: int = Path(..., ge=1, le=1000, description="ID do produto entre 1 e 1000")):
    return {"product_id": product_id}

# 4. Endpoint com Path Parameter opcional
@app.get("/optional/{item_id}")
def get_optional(item_id: Optional[int] = None):
    return {"item_id": item_id}

# 5.1 Endpoint com múltiplos Query Parameters
@app.get("/search/")
def search_users(name: Optional[str] = Query(None), min_age: Optional[int] = Query(None)):
    return {"name": name, "min_age": min_age}

# 5.2 Endpoint com múltiplos Query Parameters
@app.get("/products/")
def list_products(category: Optional[str] = Query(None), in_stock: Optional[bool] = Query(None)):
    return {"category": category, "in_stock": in_stock}

# 6.1 Endpoint que recebe Body e valida com Data Model User
@app.post("/user/")
def create_user(user: User):
    return {"message": "Usuário criado", "user": user}

# 6.2 Endpoint que recebe Body e valida com Data Model Product
@app.post("/product/")
def create_product(product: Product):
    return {"message": "Produto criado", "product": product}

# ----------------------
# CLASSES CRUD - PRODUCT
# ----------------------
class ProductCreateView:
    router = APIRouter()

    @router.post("/class/product/create", response_model=Product)
    def create(product: Product):
        products_db.append(product)
        return product

class ProductEditView:
    router = APIRouter()

    @router.put("/class/product/edit/{product_id}", response_model=Product)
    def edit(product_id: int, product: Product):
        for idx, prod in enumerate(products_db):
            if prod.id == product_id:
                products_db[idx] = product
                return product
        raise HTTPException(status_code=404, detail="Produto não encontrado")

class ProductDetailView:
    router = APIRouter()

    @router.get("/class/product/detail/{product_id}", response_model=Product)
    def detail(product_id: int):
        for prod in products_db:
            if prod.id == product_id:
                return prod
        raise HTTPException(status_code=404, detail="Produto não encontrado")

class ProductListView:
    router = APIRouter()

    @router.get("/class/product/list", response_model=List[Product])
    def list():
        return products_db

class ProductDeleteView:
    router = APIRouter()

    @router.delete("/class/product/delete/{product_id}")
    def delete(product_id: int):
        for idx, prod in enumerate(products_db):
            if prod.id == product_id:
                del products_db[idx]
                return {"message": "Produto deletado"}
        raise HTTPException(status_code=404, detail="Produto não encontrado")

# Registrar rotas das classes
app.include_router(ProductCreateView.router)
app.include_router(ProductEditView.router)
app.include_router(ProductDetailView.router)
app.include_router(ProductListView.router)
app.include_router(ProductDeleteView.router)

# ----------------------
# MÉTODOS CRUD - USER
# ----------------------
@app.post("/method/user/create", response_model=User)
def user_create(user: User):
    users_db.append(user)
    return user

@app.put("/method/user/edit/{user_id}", response_model=User)
def user_edit(user_id: int, user: User):
    for idx, u in enumerate(users_db):
        if u.id == user_id:
            users_db[idx] = user
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.get("/method/user/detail/{user_id}", response_model=User)
def user_detail(user_id: int):
    for u in users_db:
        if u.id == user_id:
            return u
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.get("/method/user/list", response_model=List[User])
def user_list():
    return users_db

@app.delete("/method/user/delete/{user_id}")
def user_delete(user_id: int):
    for idx, u in enumerate(users_db):
        if u.id == user_id:
            del users_db[idx]
            return {"message": "Usuário deletado"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
