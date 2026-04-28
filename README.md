# Makwela App User Management System

## Overview

This project is a web-based User Management System developed as part of a software development assessment.
It allows users to log in and perform full CRUD (Create, Read, Update, Delete) operations on user records, as well as export data to a Microsoft Word document.

---

##  Features

* User Login (Surname + Password)
* Add New User
* View All Users
* Edit User Details (First Name & Last Name)
* Delete User with Confirmation
* Export User Data to Microsoft Word
* Input Validation on Forms
* Clean and Responsive UI using Bootstrap

---

## Technologies Used

### Backend

* Python
* FastAPI
* SQLAlchemy

### Frontend

* HTML
* CSS (Bootstrap)
* JavaScript 

### Database

* SQLite

### Other

* python-docx (for Word export)

---

## Setup Instructions

### 1. Clone or Download Project

```
git clone <repo-link>
cd ztq-python-assessment/backend
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install fastapi uvicorn sqlalchemy python-docx
```

---

### 4. Run Backend Server

```
python -m uvicorn main:app --reload
```

Backend will run on:

```
http://127.0.0.1:8000
```

---

### 5. Open Frontend

Open `index.html` using:

* Live Server (recommended), OR
* Double click the file

---

## Testing

Test the following functionality:

* Login with valid credentials
* Attempt login with invalid credentials
* Add a new user
* Edit an existing user
* Delete a user
* Export user list to Word

---

## Database Structure

### Users Table

* UserID (Primary Key)
* Password

### UserDetails Table

* UserDetailsID (Primary Key)
* UserID (Foreign Key)
* FirstName
* LastName
* DateOfBirth
* Province
* Gender
* Facilitator

---

## Development Time

Estimated time spent:
**30 hours**

---

## Notes

* The application runs locally and is demonstrated via a live session.
* No external hosting or deployment is required.
* All functionality is implemented according to the provided specification.

---

## Conclusion

This project demonstrates the ability to:

* Build a full-stack web application
* Design and interact with a relational database
* Implement RESTful APIs
* Handle user input and validation
* Deliver a functional and user-friendly system

---
