#  TESRECO Intern Management Portal

## Assessment 1 – Advanced Python & Flask Development

The **TESRECO Intern Management Portal** is a complete web application developed as part of the TESRECO Technologies Assessment. It demonstrates practical implementation of **Advanced Python concepts**, **Flask Web Development**, **REST APIs**, **SQLite Database Integration**, and **Object-Oriented Programming (OOP)**.

The application enables organizations to efficiently manage intern registrations, mentor assignments, attendance records, and performance-related information through a centralized dashboard.

---

# 📌 Project Objectives

- Develop a modular Python application using OOP principles.
- Build RESTful APIs using Flask.
- Perform CRUD operations using SQLite.
- Demonstrate advanced Python concepts.
- Create a responsive web interface using HTML, CSS, and Jinja2.
- Follow professional project structure and GitHub practices.

---

# ✨ Features

## 🔹 Advanced Python

- Object-Oriented Programming
- Constructor, Getter & Setter Methods
- `__str__()` Method
- Function Decorators
- Custom Iterator
- Generator Functions
- Custom Exceptions
- Shallow Copy vs Deep Copy
- Multiple Inheritance
- Abstract Classes
- Functional Programming
- CSV File Handling
- Multithreading
- Multiprocessing
- Logging
- SQLite CRUD Operations

---

## 🌐 Flask Web Application

- Home Dashboard
- About Page
- Intern Registration API
- View Interns API
- Update Intern Details
- Delete Intern
- Attendance Module
- Mentor Assignment Module
- Complete CRUD Web Application
- Responsive Dashboard UI

---

# 🛠 Technologies Used

- Python 3
- Flask
- SQLite3
- HTML5
- CSS3
- Jinja2
- Git
- GitHub
- Postman

---

# 📂 Project Structure

```
Intern_Management_Portal/
│
├── app.py
├── database.py
├── interns.db
├── interns.csv
├── requirements.txt
├── README.md
├── tesreco.log
│
├── models/
│   ├── intern.py
│   ├── mentor.py
│   └── report.py
│
├── utils/
│   ├── decorator.py
│   ├── iterator.py
│   ├── generator.py
│   ├── exception.py
│   ├── copy_demo.py
│   ├── functional_programming.py
│   ├── file_handler.py
│   ├── threading_demo.py
│   ├── multiprocessing_demo.py
│   └── logger.py
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── add_intern.html
│   ├── edit_intern.html
│   └── view_interns.html
│
├── static/
│   ├── style.css
│   └── logo.jpg
│
└── postman/
    └── TESRECO_API.postman_collection.json
```

---

# ⚙ Installation

### Clone the repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory

```bash
cd Intern_Management_Portal
```

Install dependencies

```bash
pip install flask
```

or

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Create the database

```bash
python database.py
```

Run the Flask application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 🌐 REST APIs

## Register Intern

**POST**

```
/register
```

Sample Request

```json
{
    "name":"Aakash",
    "email":"akash@gmail.com",
    "domain":"Data Science",
    "duration":6
}
```

---

## View Interns

**GET**

```
/interns
```

Returns all registered interns.

---

## Update Intern

**PUT**

```
/intern/<id>
```

Updates intern information.

---

## Delete Intern

**DELETE**

```
/intern/<id>
```

Deletes an intern.

---

## Attendance Module

**POST**

```
/attendance
```

Stores attendance records.

---

## Mentor Assignment

**POST**

```
/assign-mentor
```

Assigns mentors to interns.

---

# 🗄 Database Schema

### Interns

| Column | Type |
|---------|------|
| id | INTEGER |
| name | TEXT |
| email | TEXT |
| domain | TEXT |

---

### Attendance

| Column | Type |
|---------|------|
| attendance_id | INTEGER |
| intern_id | INTEGER |
| date | TEXT |
| status | TEXT |

---

### Mentors

| Column | Type |
|---------|------|
| mentor_id | INTEGER |
| name | TEXT |
| specialization | TEXT |

---

### Mentor Assignment

| Column | Type |
|---------|------|
| id | INTEGER |
| intern_id | INTEGER |
| mentor_id | INTEGER |

---

# 📄 CSV File Handling

The application maintains intern records in **interns.csv**.

Implemented Operations:

- Add Record
- Search Record
- Delete Record

---

# 🧠 Python Concepts Demonstrated

- Classes & Objects
- Encapsulation
- Inheritance
- Multiple Inheritance
- Abstract Classes
- Decorators
- Iterators
- Generators
- Exception Handling
- Lambda Functions
- Functional Programming (`map`, `filter`, `reduce`)
- File Handling
- Logging
- SQLite Integration
- Multithreading
- Multiprocessing

---

# 🧪 API Testing

All APIs were successfully tested using **Postman**.

The exported Postman collection is available inside:

```
postman/
```

---

# 📚 Learning Outcomes

Through this assessment, I gained practical experience in:

- Developing RESTful APIs using Flask
- Applying Object-Oriented Programming concepts
- Designing modular Python applications
- Working with SQLite databases
- Implementing CRUD operations
- Using decorators, generators, iterators, and custom exceptions
- Working with multithreading and multiprocessing
- Managing projects using Git and GitHub

---

# 👩‍💻 Author

**Shambhavi Jha**

Developed as part of **TESRECO Consultancy Servicies – Assessment 1**

---

# 📜 License

This project has been developed solely for educational and assessment purposes.
