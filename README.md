#  PHP Product Management API (JWT Auth)

A RESTful API built using Core PHP with a custom MVC structure.
This project demonstrates authentication using JWT and full CRUD operations for product management.

---

##  Key Features

*  JWT-based Authentication (Login system)
*  Product CRUD API (Create, Read, Update, Delete)
*  Custom Routing System
*  MVC Architecture (Controllers, Models)
*  Lightweight & Framework-free (Core PHP)
*  Secure password handling (`password_hash`, `password_verify`)

---

##  Project Structure

```
project/
│
├── app/
│   ├── controllers/
│   │   ├── ProductController.php
│   │   └── AuthController.php
│   │
│   ├── models/
│   │   └── User.php
│
├── routes/
│   └── web.php
│
├── public/
│   └── index.php
│
├── .env
└── README.md
```

---

##  Setup Instructions

1. Clone the repository
2. Move project into XAMPP:

   ```
   C:\xampp\htdocs\
   ```
3. Start Apache & MySQL
4. Create `.env` file:

   ```
   JWT_SECRET=your_secret_key
   ```
5. Open in browser:

   ```
   http://localhost/your-project/public
   ```

---

##  Authentication (JWT)

This project uses the Firebase PHP-JWT library to generate secure tokens.

###  Login

```
POST /api/login
```

###  Request

```json
{
  "username": "admin",
  "password": "123456"
}
```

###  Response

```json
{
  "token": "your_jwt_token"
}
```

---

##  Using the Token

Include the token in request headers:

```
Authorization: Bearer <your_token>
```

---

##  Product API Endpoints

### Get All Products

```
GET /api/products
```

### Create Product

```
POST /api/products
```

### Update Product

```
PATCH /api/products
```

### Delete Product

```
DELETE /api/products
```

---

##  UI Route

```
GET /products
```

Displays product list in browser.

---

##  Tech Stack

* Core PHP
* REST API principles
* JWT Authentication
* MySQL (optional / extendable)
* Apache (XAMPP)

---

##  Current Limitations

* No middleware for token verification (needs implementation)
* Role is hardcoded (not dynamic)
* Limited validation & error handling
* Demo user (can be replaced with database)

---

##  Future Improvements

*  Add JWT middleware for route protection
*  Implement PDO + MySQL integration
*  Add role-based access control (RBAC)
*  Input validation & error handling
*  Pagination, filtering, search
*  Convert to Laravel for scalability

---


