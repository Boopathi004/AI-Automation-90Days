# 🔐 Day 19 — Authentication, OAuth2, JWT & Role-Based Authorization

## 🎯 Day 19 Goal

The goal of Day 19 was to understand how authentication and authorization work in a FastAPI application and how to secure API endpoints using OAuth2, JWT access tokens, Bearer authentication, and role-based permissions.

By the end of Day 19, I built a **Secure Employee Management API** where authenticated users can access protected endpoints and admin users receive additional permissions.

---

## 📚 Sessions Completed

| Session | Topic | Status |
|---|---|---|
| Session 1 | Authentication & Authorization Basics | ✅ Completed |
| Session 2 | FastAPI OAuth2 Login | ✅ Completed |
| Session 3 | JWT Access Tokens | ✅ Completed |
| Session 4 | Secure Employee Management API | ✅ Completed |

---

# 🟢 Session 1 — Authentication & Authorization Basics

## Authentication

Authentication verifies the identity of a user.

It answers:

> **Who are you?**

Example:

```text
Username + Password
        ↓
Verify Credentials
        ↓
Authenticated User
```

## Authorization

Authorization determines what an authenticated user is allowed to access.

It answers:

> **What are you allowed to do?**

Example:

```text
ADMIN
├── View Employees
├── Create Employees
├── Delete Employees
└── Access Admin Dashboard

USER
└── View Employees
```

### Key Difference

```text
Authentication → Who are you?
Authorization  → What can you access?
```

During Session 1, I created a simple authentication flow using:

- Username
- Password
- Role
- Credential verification

---

# 🟢 Session 2 — FastAPI OAuth2 Login

In Session 2, I moved the authentication concept into FastAPI.

## Concepts Learned

- `OAuth2PasswordRequestForm`
- `Depends()`
- FastAPI dependency injection
- Login endpoint
- Credential verification
- HTTP authentication errors
- Form-based login data

## Login Endpoint

```text
POST /login
```

Authentication flow:

```text
Username + Password
        ↓
OAuth2PasswordRequestForm
        ↓
authenticate_user()
        ↓
Valid?
   /         \
 Yes          No
  ↓            ↓
200 OK     401 Unauthorized
```

### Successful Login

Valid credentials return a successful response.

### Invalid Login

Invalid credentials return:

```text
401 Unauthorized
```

This session also helped me understand that `POST /login` only accepts POST requests, so attempting `GET /login` results in:

```text
405 Method Not Allowed
```

---

# 🟢 Session 3 — JWT Access Tokens

Session 3 introduced **JSON Web Tokens (JWT)**.

After successful authentication, the server generates an access token that can be used for future protected API requests.

## Concepts Learned

- JWT
- JWT encoding
- JWT decoding
- JWT expiration
- Bearer tokens
- `OAuth2PasswordBearer`
- Token verification
- Protected endpoints
- Current-user dependencies

---

## JWT Structure

A JWT contains three main parts:

```text
HEADER.PAYLOAD.SIGNATURE
```

### Header

Contains token metadata such as the signing algorithm.

### Payload

Contains claims such as:

```text
username
role
expiration
```

### Signature

Helps verify that the signed token has not been modified.

> JWT payloads are encoded, not automatically encrypted. Sensitive information such as passwords should never be placed inside the JWT payload.

---

## JWT Configuration

Example configuration used during learning:

```python
SECRET_KEY = "my-super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

For a production application, secret keys should be stored securely using environment variables or a secret-management solution.

---

## Creating Access Tokens

Created:

```python
create_access_token()
```

Token-generation flow:

```text
Authenticated User
       ↓
Username + Role
       ↓
Add Expiration
       ↓
JWT Encode
       ↓
Signed Access Token
```

Example token payload:

```python
{
    "sub": "admin",
    "role": "admin"
}
```

`sub` represents the **subject** of the token.

---

## OAuth2 Bearer Authentication

Configured:

```python
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)
```

Protected API requests send:

```text
Authorization: Bearer <access_token>
```

---

## Current User Validation

Created:

```python
get_current_user()
```

This dependency:

1. Receives the Bearer token.
2. Decodes the JWT.
3. Verifies the signature.
4. Checks token validity/expiration.
5. Reads the username and role.
6. Returns the authenticated user.

Flow:

```text
Bearer Token
     ↓
OAuth2PasswordBearer
     ↓
get_current_user()
     ↓
jwt.decode()
     ↓
Verify Token
     ↓
Current User
```

---

## Protected Endpoints

Created protected endpoints including:

```text
GET /profile
GET /dashboard
```

Without valid authentication, protected resources are rejected.

---

# 🟢 Session 4 — Secure Employee Management API

The final session combined the Day 19 concepts into one practical mini project.

# 🚀 Project — Secure Employee Management API

The project demonstrates:

- FastAPI backend development
- OAuth2 login
- JWT access-token generation
- Bearer authentication
- Protected routes
- Current-user validation
- Role-based authorization
- Employee management
- Admin-only operations
- HTTP exception handling

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Pydantic
- OAuth2
- JWT
- PyJWT
- Uvicorn
- Swagger UI
- FastAPI Dependency Injection

---

## 📌 API Endpoints

| Method | Endpoint | Access |
|---|---|---|
| `POST` | `/login` | Public |
| `GET` | `/profile` | Authenticated |
| `GET` | `/employees` | Authenticated |
| `POST` | `/employees` | Admin Only |
| `DELETE` | `/employees/{employee_id}` | Admin Only |
| `GET` | `/admin/dashboard` | Admin Only |

---

# 🛡️ Role-Based Authorization

Two roles were implemented:

## Admin

Admin users can:

- Login
- Access their profile
- View employees
- Create employees
- Delete employees
- Access the admin dashboard

## Normal User

Normal users can:

- Login
- Access their profile
- View employees

Normal users cannot:

- Create employees
- Delete employees
- Access the admin dashboard

---

## Admin Authorization Dependency

Created:

```python
require_admin()
```

Authorization flow:

```text
Authenticated User
       ↓
Check Role
       ↓
Is role admin?
    /        \
  YES         NO
   ↓           ↓
Allow      403 Forbidden
```

This separates:

```text
Authentication
      ↓
Is this a valid user?

Authorization
      ↓
Does this user have permission?
```

---

# ⚠️ HTTP Status Codes Practiced

## `200 OK`

The request completed successfully.

Examples:

```text
POST /login
GET /employees
GET /admin/dashboard
DELETE /employees/102
```

when the request and permissions are valid.

---

## `401 Unauthorized`

Used when authentication is missing, invalid, or expired.

Example:

```text
Protected endpoint
       ↓
No valid JWT
       ↓
401 Unauthorized
```

---

## `403 Forbidden`

Used when the user is authenticated but does not have the required permission.

Example:

```text
Normal User
    ↓
Admin Endpoint
    ↓
403 Forbidden
```

---

## `404 Not Found`

Used when the requested resource cannot be found.

Example:

```text
DELETE /employees/999
        ↓
Employee doesn't exist
        ↓
404 Not Found
```

---

# 🔐 Complete Authentication Architecture

```text
Client
  ↓
POST /login
  ↓
Username + Password
  ↓
authenticate_user()
  ↓
Credential Verification
  ↓
create_access_token()
  ↓
JWT Access Token
  ↓
Client Sends Bearer Token
  ↓
OAuth2PasswordBearer
  ↓
get_current_user()
  ↓
Decode + Verify JWT
  ↓
Authenticated User
  ↓
Role Check
  ↓
Authorization
  ↓
Protected API
```

---

# 📊 Permissions Matrix

| Feature | Admin | User |
|---|:---:|:---:|
| Login | ✅ | ✅ |
| View Profile | ✅ | ✅ |
| View Employees | ✅ | ✅ |
| Create Employee | ✅ | ❌ |
| Delete Employee | ✅ | ❌ |
| Admin Dashboard | ✅ | ❌ |

---

# 🧪 Testing Completed

The API was tested through Swagger UI.

### Authentication Tests

```text
Valid login            → 200 OK
Invalid credentials    → 401 Unauthorized
No valid authentication→ 401 Unauthorized
```

### Authorization Tests

```text
Admin → Admin Dashboard → 200 OK
User  → Admin Dashboard → 403 Forbidden
Admin → Create Employee → Allowed
User  → Create Employee → 403 Forbidden
Admin → Delete Employee → Allowed
User  → Delete Employee → 403 Forbidden
```

### Resource Test

```text
Unknown Employee → 404 Not Found
```

---

# 💡 Key Learning

Day 19 showed that building a backend API is not only about creating CRUD endpoints.

Real applications also require:

```text
Authentication
      +
Token Management
      +
Protected Routes
      +
Authorization
      +
Error Handling
```

These concepts are especially important when building secure:

- AI APIs
- RAG applications
- AI agents
- Automation services
- Backend applications
- Internal business tools

---

# 🎯 Interview Preparation

## What is Authentication?

Authentication verifies the identity of a user.

---

## What is Authorization?

Authorization determines what an authenticated user is permitted to access or perform.

---

## What is JWT?

JWT stands for **JSON Web Token**. It can carry signed claims between a client and server and is commonly used as an access token in API authentication systems.

---

## What are the three parts of JWT?

```text
Header
Payload
Signature
```

---

## What is a Bearer Token?

A Bearer token is an access token supplied through the HTTP Authorization header.

```text
Authorization: Bearer <token>
```

---

## What is `Depends()` in FastAPI?

`Depends()` is FastAPI's dependency injection mechanism.

It can be used for reusable logic such as:

- Authentication
- Authorization
- Database connections
- Current-user retrieval

---

## What is the difference between 401 and 403?

```text
401 Unauthorized
→ Authentication is missing or invalid.

403 Forbidden
→ Authentication succeeded, but permission is insufficient.
```

---

# 🔒 Production Security Improvements

The Day 19 application is a learning project.

The demo implementation uses in-memory users and simple demo passwords.

A production implementation should additionally include:

- Password hashing
- Secure password verification
- Environment variables for secret keys
- Persistent user database
- Strong JWT secret/key management
- Token expiration policies
- Refresh-token strategy where appropriate
- Revocation/session strategy where required
- HTTPS
- Input validation
- Logging and monitoring

---

# 🏆 Day 19 Achievement

By completing Day 19, I moved from building standard FastAPI endpoints to building an API with an authentication and authorization layer.

```text
FastAPI
   ↓
OAuth2 Login
   ↓
JWT Access Token
   ↓
Bearer Authentication
   ↓
Protected Routes
   ↓
Role-Based Authorization
   ↓
Secure Employee Management API
```

---

## ✅ Day 19 Completion Checklist

- [x] Authentication fundamentals
- [x] Authorization fundamentals
- [x] User roles
- [x] FastAPI login endpoint
- [x] `OAuth2PasswordRequestForm`
- [x] `Depends()`
- [x] JWT concepts
- [x] JWT generation
- [x] JWT expiration
- [x] Bearer authentication
- [x] JWT decoding and verification
- [x] Current-user dependency
- [x] Protected endpoints
- [x] Role-based authorization
- [x] Admin-only routes
- [x] `401 Unauthorized`
- [x] `403 Forbidden`
- [x] `404 Not Found`
- [x] Swagger UI testing
- [x] Secure Employee Management API mini project

---

# 📈 Day 19 Status

**Day 19 — Completed Successfully ✅**

### Final Project

**Secure Employee Management API**

### Core Skills

**FastAPI + OAuth2 + JWT + Bearer Authentication + Dependency Injection + Role-Based Authorization**

---

## 🚀 Next Step

Continue the **AI Automation Engineer learning journey with Day 20**, building on the secure backend foundation developed during Day 19.
