# 🧑‍🎓 Student Record Management System (Django)

This project is a **beginner-friendly yet practical Django application** designed to help you understand and implement essential backend concepts like **forms, CRUD operations, and template management**.

---

## 🎯 Objective

Build a simple **web-based system** to manage student records, including the ability to **create, read, update, and delete** information using Django features such as:

- HTML Forms & Model Forms  
- Class-Based Views  
- Template Inheritance  

---

## 🚀 Key Features

### 1. 📝 Student Registration
- Collect basic student information:
  - Name, Email, Phone Number, Course
- Built with **HTML Forms** and enhanced using **HTML5 validations** (e.g., required fields, valid email format).

### 2. 📋 Student List Page
- Display all registered students in a clean layout.
- Use **reusable templates** to render dynamic student data.

### 3. 🔁 CRUD Operations
- **Create**: Add a new student using **Model Forms**.
- **Read**: View individual student details on a dedicated page.
- **Update**: Edit student information using **GET & POST requests**.
- **Delete**: Remove student entries via **DELETE request** (confirmation included).

### 4. 🧩 Template Features
- Implement **template inheritance** with `base.html` for consistent navbar, footer, etc.
- Use **template blocks** to easily customize sections like:
  - Form rendering  
  - Student listing  
  - Message notifications

### 5. ✅ Message Framework
- Display feedback with Django’s built-in **message framework**:
  - Success: “Student added successfully.”
  - Error: “Unable to delete student.”

---

## 🛠️ Tools & Technologies

| Area        | Tools/Technologies              |
|-------------|---------------------------------|
| Frontend    | HTML, CSS (optional styling)    |
| Backend     | Django (forms, views, templates)|
| Database    | SQLite (Django's default DB)    |

---

## 📁 Folder Structure (Suggested)
```
student_project/
├── student_app/
│   ├── templates/
│   │   ├── base.html
│   │   ├── student_list.html
│   │   ├── student_form.html
│   │   ├── student_detail.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
├── student_project/
│   ├── settings.py
│   ├── urls.py
```

---

## 🧪 Ideal For
- Django Beginners  
- Students building portfolio projects  
- Developers learning CRUD and form handling in Django

---

## 📌 Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/student-record-system.git
   cd student-record-system
   ```

2. Set up the virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install Django:
   ```bash
   pip install django
   ```

4. Run the server:
   ```bash
   python manage.py runserver
   ```

---

Feel free to customize and expand the project for your learning goals! 😊
