from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product 
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_methods = ["*"],
    allow_credentials = True
)

database_models.Base.metadata.create_all(bind = engine)

def get_db():
    db = session()
    try:
     yield db
    finally:
     db.close()

@app.get("/")
def greet():
    return "Welcome to this page"

products = [
    Product(id = 1,name = "Phone", description = "Budget Phone", price= 99,quantity= 10),
    Product(id = 2, name = "Laptop", description = "Gaming Laptop", price= 999,quantity =  6),
    Product(id = 3, name = "Shampoo", description= "Hair Shampoo", price = 5.65, quantity = 5),
    Product(id = 4, name = "Pencil", description= "To Write With", price = 1.00, quantity = 50),
    Product(id = 5, name = "Notebook", description= "To write On", price = 2.50, quantity = 50)
]

def init_db():
    db = session()
    count = db.query(database_models.Product).count()
    if count == 0:
     for product in products:
        db.add(database_models.Product(**product.model_dump()))
        
    db.commit()
init_db()

@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
       return db_product   
    return "Product Not Found"


@app.post("/products/")
def add_product(product: Product, db:Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        db.add(database_models.Product(**product.model_dump()))
        db.commit()
        return product
    return f"No product found with id {id}"


@app.delete("/products/{id}")
def delete_product(id:int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Successfully Deleted" 
    else:
     return "No product found for deletion"