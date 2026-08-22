from datetime import datetime, timedelta, timezone

import jwt

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import (
    OAuth2PasswordRequestForm,
    OAuth2PasswordBearer
)



app = FastAPI(
    title="Authentication API",
    version="1.0.0"
)

SECRET_KEY = "my-super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


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

    access_token = create_access_token(
        {
            "sub": user["username"],
            "role": user["role"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
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
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)
def create_access_token(data: dict):

    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({
        "exp": expire
    })

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token
def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        return {
            "username": username,
            "role": payload.get("role")
        }

    except jwt.InvalidTokenError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
@app.get("/profile")
def profile(
    current_user: dict = Depends(get_current_user)
):

    return {
        "message": "Protected profile accessed",
        "username": current_user["username"],
        "role": current_user["role"]
    }