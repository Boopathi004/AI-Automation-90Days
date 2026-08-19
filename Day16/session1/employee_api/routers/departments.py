from fastapi import APIRouter

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.get("/")
def get_departments():
    return {
        "departments": ["AI Engineering", "HR", "IT"]
    }