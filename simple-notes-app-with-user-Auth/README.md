# Notes App with User Authentication (Django)

This is a simple Notes App built using **Django** with basic user authentication and note management (CRUD operations).  
It is designed as a learning project to practice **custom user models**, **form customization**, and **CRUD functionality** in Django.

---

## 🛠 Features

- User Authentication (Sign up, Login, Logout)
- Custom User Model (extended from `AbstractUser`) with an additional `address` field
- Customized Django Admin (`CustomUserAdmin`)
- Custom User Registration Form (`CustomUserCreationForm`)
- Custom Login Form
- Notes Management (CRUD):
  - Create a new note
  - Edit an existing note
  - Delete a note
  - View all notes belonging to the **logged-in user** on the dashboard
- Secure user sessions (users can only access their own notes

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python), SQLite database

---

## 🚀 How to Run the Project Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/notes-app-django.git
   cd notes-app-django
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the app**
   - Open your browser and visit: `http://127.0.0.1:8000/`

---

## 🎯 Learning Outcomes of Project

This project was created as a **learning exercise** to:

- Understand the importance of **custom user models** early in Django projects
- Explore how Django’s authentication system works behind the scenes
- Practice handling **basic CRUD operations** securely
- Strengthen skills in **form handling** and **template rendering**
- Build a complete **full-stack web application** using Django

It is an ideal **beginner to intermediate** level project for anyone learning Django and web development.
