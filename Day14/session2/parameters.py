from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Day 14 - Session 2"
    }


# Path Parameter
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return {
        "employee_id": employee_id,
        "message": "Employee found"
    }


# Query Parameter
@app.get("/search")
def search_employee(name: str):
    return {
        "search_name": name,
        "message": "Searching employee"
    }

#Products 
@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
  "product_id": product_id,
  "product_name": "Laptop",
  "price": 55000
}