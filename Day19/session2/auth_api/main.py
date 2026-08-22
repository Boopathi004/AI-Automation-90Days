from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI(
    title="Authentication API",
    version="1.0.0"
)


# --------------------------------
# Demo Users Database
# --------------------------------

users_db = {
    "admin": {
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "username": "user",
        "password": "user123",
        "role": "user"
    },
    "manager": {
        "username": "manager",
        "password": "manager123",
        "role": "manager"
    }
}


# --------------------------------
# Home Route
# --------------------------------

@app.get("/")
def home():
    return {
        "message": "Authentication API is running"
    }


# --------------------------------
# Authentication Function
# --------------------------------

def authenticate_user(username: str, password: str):

    user = users_db.get(username)

    if not user:
        return None

    if user["password"] != password:
        return None

    return user


# --------------------------------
# Login Route
# --------------------------------

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    user = authenticate_user(
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    return {
        "message": "Login successful",
        "username": user["username"],
        "role": user["role"]
    }


# --------------------------------
# Get User Route
# --------------------------------

@app.get("/users/{username}")
def get_user(username: str):

    user = users_db.get(username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "username": user["username"],
        "role": user["role"]
    }