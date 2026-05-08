# CertifyMe — Full Stack Intern Assessment

## Overview

CertifyMe is a full-stack web application for the Qatar Foundation Admin Portal. It provides a secure backend API for user authentication and opportunity management, integrated with an existing frontend interface. The project demonstrates modern web development practices with Flask, SQLAlchemy, JWT authentication, and a responsive HTML/CSS/JS frontend.

## Features

### Backend
- **User Authentication**: Secure signup, login, password reset with JWT tokens
- **Opportunity Management**: Full CRUD operations for opportunities with user-specific access
- **Database Integration**: SQLite with SQLAlchemy ORM (easily configurable for PostgreSQL/MySQL)
- **Security**: Password hashing with Bcrypt, secure token generation, CORS support
- **API Design**: RESTful endpoints with proper validation and error handling

### Frontend
- Admin dashboard for opportunity management
- User authentication forms (signup, login, forgot password)
- Dynamic opportunity cards with create, edit, and delete functionality
- API integration with JWT token management

## Tech Stack

### Backend
- **Flask** 3.0.2 - Web framework
- **Flask-SQLAlchemy** 3.1.1 - ORM
- **Flask-JWT-Extended** 4.6.0 - JWT authentication
- **Flask-Bcrypt** 1.0.1 - Password hashing
- **Flask-CORS** 4.0.0 - Cross-origin resource sharing
- **Python-Dotenv** 1.0.1 - Environment variables
- **ItsDangerous** 2.2.0 - Secure token generation

### Frontend
- HTML5, CSS3, JavaScript (ES6+)

### Database & Tools
- SQLite (development) / PostgreSQL (production)
- Git for version control

## Installation

### Prerequisites
- Python 3.8+
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/SriDeekshith24/Myrepo.git
   cd Myrepo
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   Create a `.env` file in the `backend/` directory:
   ```env
   SECRET_KEY=your-secret-key-here
   JWT_SECRET_KEY=your-jwt-secret-key-here
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```
   The backend server will start at `http://127.0.0.1:5000`

5. **Frontend Access**
   Open `sky/admin.html` in your browser to access the frontend interface.

## Usage

1. **Signup**: Create a new admin account
2. **Login**: Authenticate and receive a JWT token
3. **Manage Opportunities**: Create, view, edit, and delete opportunities
4. **Password Reset**: Use forgot password functionality for account recovery

## API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/signup` | Register new user |
| POST | `/api/auth/login` | User login with JWT |
| POST | `/api/auth/forgot-password` | Request password reset |
| POST | `/api/auth/reset-password/<token>` | Reset password with token |

### Opportunity Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/opportunities` | Get all user opportunities |
| POST | `/api/opportunities` | Create new opportunity |
| GET | `/api/opportunities/<id>` | Get specific opportunity |
| PUT | `/api/opportunities/<id>` | Update opportunity |
| DELETE | `/api/opportunities/<id>` | Delete opportunity |

**Authentication**: Protected endpoints require `Authorization: Bearer <token>` header.

## Project Structure

```
Myrepo/
├── README.md
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── config.py              # Configuration settings
│   ├── extensions.py          # Flask extensions
│   ├── requirements.txt       # Python dependencies
│   ├── .env                   # Environment variables
│   ├── instance/
│   │   └── database.db        # SQLite database
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py            # User model
│   │   └── opportunity.py     # Opportunity model
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py     # Authentication endpoints
│   │   └── opportunity_routes.py # Opportunity endpoints
│   └── utils/
│       ├── __init__.py
│       ├── validators.py      # Input validation
│       └── token_helper.py    # Token utilities
└── sky/
    ├── admin.html             # Main admin interface
    ├── admin.css              # Styles
    └── admin.js               # Frontend logic
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- **Author**: Sai Deekshith
- **Email**: srideekshith@gmail.com
- **GitHub**: [SriDeekshith24](https://github.com/SriDeekshith24)

### 🔗 Original Repository
[https://github.com/Neerajvs32/Test1](https://github.com/Neerajvs32/Test1)

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python |
| Framework | Flask |
| Database | SQLite / MySQL / PostgreSQL |
| Frontend | Pre-built Admin UI |

---

## 🧩 Features & User Stories

---

### ✅ Task 1 — Authentication *(Day 1)*

---

#### US-1.1 — Admin Sign Up

**Required Fields**
- Full Name
- Email
- Password
- Confirm Password

**Validations**
- All fields mandatory
- Email must be valid
- Password minimum 8 characters
- Passwords must match
- Email must be unique

**Expected Result**
- Save admin account
- Redirect to Login page

---

#### US-1.2 — Admin Login

**Fields**
- Email
- Password
- Remember Me checkbox

**Rules**
- Show generic error on failure:
  ```
  Invalid email or password
  ```

**Expected Result**
- Redirect to dashboard
- Load opportunities created by the admin

**Session Handling**

| Condition | Behaviour |
|---|---|
| Remember Me checked | Long-lived session |
| Remember Me unchecked | Session ends when browser closes |

---

#### US-1.3 — Forgot Password

**Requirements**
- Admin enters their email
- Always show the same success message (regardless of whether email exists)

**Behaviour**
- Generate reset link internally
- No email sending required

**Security**
- Reset link expires after **1 hour**
- Expired link shows an error

---

### ✅ Task 2 — Opportunity Management *(Day 2)*

> All opportunities must be stored in the database, linked to the logged-in admin, and must never use hardcoded data.

---

#### US-2.1 — View All Opportunities

**Each opportunity card must display:**
- Opportunity Name
- Category
- Duration
- Start Date
- Description

**Rules**
- Show only the logged-in admin's opportunities
- Remove all demo / hardcoded cards
- Show an empty state if no opportunities exist

---

#### US-2.2 — Add New Opportunity

**Required Fields**
- Opportunity Name
- Duration
- Start Date
- Description
- Skills to Gain *(comma separated)*
- Category
- Future Opportunities

**Optional Field**
- Maximum Applicants

**Category Options**
- Technology
- Business
- Design
- Marketing
- Data Science
- Other

**Expected Result**
- Validate all required fields
- Save opportunity to database
- Link opportunity to logged-in admin
- Display immediately **without page refresh**

---

#### US-2.3 — Opportunities Persist After Login

- Opportunities must load after logout / login cycles
- Stored only in the database — **no local storage usage**
- Admins cannot access other admins' data

---

#### US-2.4 — View Opportunity Details

- Open a details modal
- Show all saved fields
- Close button available

---

#### US-2.5 — Edit Opportunity

- Edit button opens a pre-filled form
- Apply the same validations as during creation
- Update only the selected opportunity
- Reflect changes instantly **without page refresh**

---

#### US-2.6 — Delete Opportunity

- Show a confirmation dialog before deletion
- Delete permanently from the database
- Remove from UI immediately **without page refresh**
- Only the creator admin can delete their own opportunity
#   M y r e p o 
 
 #   M y r e p o 
 
 