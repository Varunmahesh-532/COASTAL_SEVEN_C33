from fastapi import FastAPI

app = FastAPI()

products = [
    "Phone",
    "Power Bank",
    "Printer",
    "Laptop",
    "Pen",
    "Mouse",
    "Projector"
]

@app.get("/search")
def search_products(query: str):
    result = []
    for product in products:
        if product.lower().startswith(query.lower()):
            result.append(product)
    return result
