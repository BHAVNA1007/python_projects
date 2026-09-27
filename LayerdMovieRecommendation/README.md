Create this file in your project root:

MovieRecommendation/
│
├── main.py
├── model/
├── dao/
├── service/
├── database/
├── utils/
└── README.md

Use this content:

# Movie Recommendation System

## 📌 Project Overview

The Movie Recommendation System is a Python-based application that allows users to manage movies, maintain their watchlists, and receive movie recommendations based on the genres of movies in their watchlist.

The project is developed using Python, MySQL, Object-Oriented Programming, and a layered architecture.

---

## 🎯 Features

- User registration
- User login
- Get user details by ID
- Update user name
- Delete user
- Add movies
- View all movies
- Search movies by title
- Update movie title
- Delete movies
- Add movies to watchlist
- View watchlist
- Update watchlist status
- Remove movies from watchlist
- Generate movie recommendations
- Input validation
- Database error handling

---

## 🛠️ Technologies Used

- Python
- MySQL
- MySQL Connector/Python
- Object-Oriented Programming
- Layered Architecture
- SQL
- VS Code / PyCharm

---

## 🏗️ Project Architecture

The project follows a layered architecture:

```text
main.py
   ↓
Service Layer
   ↓
DAO Layer
   ↓
Database Layer
   ↓
MySQL
Model Layer

Contains classes representing application entities.

Examples:

Movie
User
Watchlist
Service Layer

Contains the application/service logic and communicates with the DAO layer.

DAO Layer

DAO stands for Data Access Object.

It is responsible for communicating with the database and executing SQL queries.

Examples:

MovieDao
UserDao
WatchlistDao
RecommendationDao
Database Layer

Contains the database connection logic.

Utils Layer

Contains reusable validation functions such as:

ID validation
Required-field validation
Rating validation
Release-year validation
Menu-choice validation
Status validation
📂 Project Structure
MovieRecommendation/
│
├── main.py
│
├── model/
│   ├── __init__.py
│   ├── movie.py
│   ├── user.py
│   └── watchlist.py
│
├── dao/
│   ├── __init__.py
│   ├── movie_dao.py
│   ├── user_dao.py
│   ├── watchlist_dao.py
│   └── recommendation_dao.py
│
├── service/
│   ├── __init__.py
│   ├── movie_service.py
│   ├── user_service.py
│   ├── watchlist_service.py
│   └── recommendation_service.py
│
├── database/
│   ├── __init__.py
│   └── connection.py
│
├── utils/
│   ├── __init__.py
│   └── validators.py
│
└── README.md
🗄️ Database

The application uses MySQL.

Database
movie_recommendation
Tables
Users

Stores registered user information.

user_id
name
email
password
Movies

Stores movie information.

movie_id
title
genre
rating
release_year
Watchlist

Stores movies added by users.

watchlist_id
user_id
movie_id
status

The watchlist table uses foreign keys to establish relationships with the users and movies tables.

🎬 Recommendation Logic

The recommendation system works based on the genres of movies already present in the user's watchlist.

The basic flow is:

User
  ↓
Watchlist
  ↓
Find genres of watchlist movies
  ↓
Find movies with matching genres
  ↓
Exclude movies already in watchlist
  ↓
Return recommendations

For example, if a user's watchlist contains a Sci-Fi movie, the system can recommend other Sci-Fi movies that are not already in that user's watchlist.

✅ Input Validation

The application validates user input before sending it to the database.

Examples:

IDs must be positive numbers
Required fields cannot be empty
Movie rating must be between 0 and 10
Release year must be valid
Menu choices must be within the allowed range
Watchlist status must be a valid status

The general validation flow is:

INPUT
  ↓
VALIDATE
  ↓
CONVERT
  ↓
USE
⚠️ Error Handling

The application handles database-related errors such as duplicate email registration.

For example, because the user email is unique, registering the same email again produces a user-friendly message instead of crashing the application.

Email already registered
▶️ How to Run
1. Install Python

Make sure Python is installed on your system.

Check the version:

python --version
2. Install MySQL Connector
pip install mysql-connector-python
3. Create the MySQL Database

Create the database:

CREATE DATABASE movie_recommendation;

Then create the required tables.

4. Configure Database Connection

Update the database connection details in:

database/connection.py
5. Run the Application

From the project directory:

python main.py
🖥️ Application Menu
========== MOVIE RECOMMENDATION SYSTEM ==========

1. User Management
2. Movie Management
3. Watchlist
4. Recommendations
5. Exit
📚 Concepts Used

This project helped me practice:

Python
OOP
Classes and Objects
Encapsulation
Modules and Packages
Exception Handling
MySQL
SQL CRUD operations
Joins
Subqueries
Foreign Keys
Unique Constraints
Transactions
Layered Architecture
DAO Pattern
Input Validation
🚀 Future Enhancements

Possible future improvements include:

Tkinter-based graphical interface
Voice-based movie search
Pandas-based movie analysis
More advanced recommendation logic
Movie filtering and sorting





👩‍💻 Author

Bhavna

MCA Graduate | Python | MySQL | Web Development


### One important README point

Don't put your **real MySQL password** in the README or GitHub repository.

Your `connection.py` should also ideally use a placeholder before uploading:

```python
password="YOUR_PASSWORD"

so your credentials aren't exposed.