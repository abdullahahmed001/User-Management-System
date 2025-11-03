# UserHub - Mini Flask User Management App

## Overview
**UserHub** is a simple web application built with **Flask** and **SQLAlchemy** that allows you to manage users.  
It demonstrates basic CRUD (Create, Read, Delete) operations and supports both **browser forms** and **JSON API requests**.

This project is designed as a learning tool for understanding Flask, SQLAlchemy, and web application concepts.

---

## Features
- **Add Users**  
  - Add a single user via browser form or JSON API.
  - Each user requires a **username**, **email**, and **password**.

- **Search Users**  
  - Search users by email via browser or API.

- **Delete Users**  
  - Delete a user by email via browser form or API request.

- **List Users**  
  - View all users currently stored in the database (JSON API).

- **Flexible Input**  
  - Supports form submissions (`application/x-www-form-urlencoded`) and JSON payloads (`application/json`).

---

## Technologies Used
- **Python 3.12**  
- **Flask** – Web framework  
- **Flask SQLAlchemy** – ORM for database management  
- **SQLite** – Lightweight database  

---

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd <project-folder>
