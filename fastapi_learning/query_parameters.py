from fastapi import FastAPI

app = FastAPI()

products = [
    {
        "id" : 1,
        "name": "Laptop",
        "brand": "HP"
    },
    {
        "id": 2,
        "name": "shirt",
        "brand": "PUMA"
    },
    {
        "id": 3,
        "name": "Bike",
        "brand": "Hero"
    }
]

#Home Route
@app.get('/')
def home():
    return {
        "Welcome to query parameter example"
    }

#Query Parameter Example
@app.get('/products')
def get_products(brand: str = None): # str = None is the main point it make it optional
    if brand:
        filter_products = []
        for product in products:
            if product['brand'] == brand:
                filter_products.append(product)

        return {
            "Filtered Products": filter_products
        }
    return {
        "pall_products": roducts
    }

