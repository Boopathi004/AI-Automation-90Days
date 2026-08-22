from pydantic import BaseModel


# User model
class User(BaseModel):
    username: str
    password: str
    role: str


# Authentication function
def authenticate_user(user: User):
    # Admin credentials
    if (
        user.username == "admin"
        and user.password == "admin123"
    ):
        return {
            "message": "Login successful",
            "username": user.username,
            "role": user.role
        }

    # Normal user credentials
    if (
        user.username == "user"
        and user.password == "user123"
    ):
        return {
            "message": "Login successful",
            "username": user.username,
            "role": user.role
        }

    # Invalid credentials
    return {
        "message": "Invalid username or password"
    }


# -----------------------------
# Test 1 - Admin Login
# -----------------------------

admin = User(
    username="admin",
    password="admin123",
    role="admin"
)

result = authenticate_user(admin)

print("Admin Login:")
print(result)


# -----------------------------
# Test 2 - Normal User Login
# -----------------------------

normal_user = User(
    username="user",
    password="user123",
    role="user"
)

result = authenticate_user(normal_user)

print("\nUser Login:")
print(result)


# -----------------------------
# Test 3 - Wrong Password
# -----------------------------

wrong_user = User(
    username="admin",
    password="wrongpassword",
    role="admin"
)

result = authenticate_user(wrong_user)

print("\nWrong Password:")
print(result)