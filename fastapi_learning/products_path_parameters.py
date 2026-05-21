from fastapi import FastAPI

app = FastAPI()

products ={
    1:{
        "name": "Laptop",
        "price": 55000,
        "brand": "HP"
    },
    2:{
        "name": "HEAD PHONES",
        "price": 2000,
        "brand": "BoaT"
    },
    3:{
        "name": "Phone",
        "price": 25000,
        "brand": "Real Me"
    }
}

#Home Route
@app.get('/')
def home():
    return {
        "Welcoem TO Product API"
    }

#ALL Products
@app.get('/product')
def all_product():
    return products

#Give the single product
@app.get("/products/{product_id}")
def product_by_id(product_id: int):
    product = products.get(product_id)
    if product:
        return product
    return {
        f"The product is not available with the specific id:{product_id}"
    }