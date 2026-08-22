# Day 19 Notes — FastAPI Authentication & JWT

## 1. Authentication

Authentication verifies the identity of a user.

**Authentication = Who are you?**

The server verifies the username and password before allowing authenticated access.

---

## 2. Authorization

Authorization determines what an authenticated user is allowed to access.

**Authorization = What can you do?**

Example:

```text
ADMIN
- View Employees
- Create Employees
- Delete Employees
- Admin Dashboard

USER
- View Employees
```

Authentication happens before authorization.

---

## 3. OAuth2PasswordRequestForm

FastAPI provides:

```python
from fastapi.security import OAuth2PasswordRequestForm
```

Usage:

```python
form_data: OAuth2PasswordRequestForm = Depends()
```

Credentials:

```python
form_data.username
form_data.password
```

---

## 4. Depends()

`Depends()` is FastAPI's dependency injection system.

Example:

```python
current_user: dict = Depends(get_current_user)
```

Common uses:

- Authentication
- Authorization
- Database sessions
- Current-user retrieval
- Shared API logic

---

## 5. JWT

JWT means **JSON Web Token**.

JWT structure:

```text
HEADER.PAYLOAD.SIGNATURE
```

### Header
Contains token metadata such as the signing algorithm.

### Payload
Contains claims such as username, role, and expiration.

### Signature
Helps verify that the signed token has not been modified.

Important: JWT payloads are encoded, not automatically encrypted. Never put passwords or secrets inside a JWT payload.

---

## 6. JWT Configuration

```python
SECRET_KEY = "my-super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

For production applications, secret keys should not be hard-coded in source code.

---

## 7. Creating Access Tokens

Function:

```python
create_access_token()
```

Flow:

```text
User Data
   +
Expiration
   ↓
JWT Encode
   ↓
Secret Key
   ↓
Access Token
```

Example payload:

```python
{
    "sub": "admin",
    "role": "admin"
}
```

`sub` means **subject** and identifies the user represented by the token.

---

## 8. Bearer Authentication

FastAPI provides:

```python
OAuth2PasswordBearer
```

Example:

```python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
```

Protected requests send:

```text
Authorization: Bearer <access_token>
```

---

## 9. Token Verification

The server decodes the token using:

```python
jwt.decode()
```

Flow:

```text
Bearer Token
    ↓
get_current_user()
    ↓
jwt.decode()
    ↓
Verify Token
    ↓
Read Username + Role
    ↓
Current User
```

Invalid or expired tokens are rejected.

---

## 10. Protected Endpoints

Example:

```python
@app.get("/profile")
def profile(
    current_user: dict = Depends(get_current_user)
):
    return {
        "username": current_user["username"],
        "role": current_user["role"]
    }
```

The endpoint requires a valid authenticated user.

---

## 11. Role-Based Authorization

Created:

```python
require_admin()
```

Logic:

```text
Authenticated User
       ↓
Check Role
       ↓
role == admin?
   YES → Allow
   NO  → 403 Forbidden
```

Example:

```python
if current_user["role"] != "admin":
    raise HTTPException(
        status_code=403,
        detail="Admin access required"
    )
```

---

## 12. HTTP Status Codes

- `200 OK` — Request completed successfully.
- `401 Unauthorized` — Authentication is missing, invalid, or expired.
- `403 Forbidden` — User is authenticated but does not have permission.
- `404 Not Found` — Requested resource does not exist.

---

## 13. Secure Employee Management API

Final Session 4 project:

```text
POST   /login
GET    /profile
GET    /employees
POST   /employees
DELETE /employees/{employee_id}
GET    /admin/dashboard
```

### Permissions

| API | Admin | User |
|---|---|---|
| Login | Yes | Yes |
| Profile | Yes | Yes |
| View Employees | Yes | Yes |
| Create Employee | Yes | No |
| Delete Employee | Yes | No |
| Admin Dashboard | Yes | No |

---

## 14. Final Authentication Flow

```text
User
 ↓
Login
 ↓
Username + Password
 ↓
Authenticate Credentials
 ↓
Generate JWT
 ↓
Access Token
 ↓
Bearer Token
 ↓
Verify JWT
 ↓
Get Current User
 ↓
Check Role
 ↓
Protected API
```

---

# Interview Notes

### Q1. What is authentication?
Authentication verifies who the user is.

### Q2. What is authorization?
Authorization determines what an authenticated user is allowed to access.

### Q3. What is JWT?
JWT stands for JSON Web Token. It can be used to carry signed claims between a client and server.

### Q4. What are the three parts of JWT?
Header, Payload, and Signature.

### Q5. What is a Bearer token?
A Bearer token is an access token sent in the HTTP Authorization header.

```text
Authorization: Bearer <token>
```

### Q6. What is the difference between 401 and 403?

```text
401 → Authentication problem
403 → Permission/authorization problem
```

### Q7. What does Depends() do?
`Depends()` is FastAPI's dependency injection mechanism. It allows reusable logic such as authentication and authorization to run before an endpoint.

---

# Security Note

The Day 19 project is a learning project and uses simple in-memory users and plain-text demo passwords.

A production system should additionally use:

- Password hashing
- Environment variables for secrets
- Persistent user database
- Strong secret/key management
- Proper token lifecycle management
- Appropriate access/refresh token strategy

---

# Day 19 Completed

Day 19 covered:

**OAuth2 Login → JWT → Bearer Authentication → Protected Routes → Role-Based Authorization**

This provides an important foundation for securing future AI Automation, RAG, Agent, and backend API projects.
