from fastapi import FastAPI
from routers.employee import router as employee_router
from routers.departments import router as department_router
from Database.connection import create_table, insert_sample_data

app = FastAPI(
    title="Employee Management API",
    version="1.0.0"
)

create_table()
insert_sample_data()

app.include_router(employee_router)
app.include_router(department_router)


@app.get("/")
def home():
    return {
        "message": "Employee API is running",
        "day": 16
    }