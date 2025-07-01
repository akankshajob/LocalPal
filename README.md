🌟 LocalPal

_LocalPal: Helping you feel at home, wherever you are._

---

🏠 Overview

LocalPal is a community-driven platform designed to help newcomers and residents explore local facilities — including cafes, restaurants, accommodations, medical services, and attractions — with ease. Think of it as your digital local companion that bridges the gap between people and the resources they need in a new place.

---

✨ Features

✅ User registration and login with secure authentication  
✅ Admin dashboard using Django’s built-in admin  
✅ Dynamic facility listings (cafes, medical, accommodation, attractions)  
✅ Filters for category and rating  
✅ User feedback forms for each facility  
✅ Responsive, modern user interface with Bootstrap and custom CSS  
✅ Feedback stored for better community interaction  
✅ MongoDB-ready (future proofing your NoSQL needs)

---

🛠 Tech Stack

- Backend: Django (Python)
- Frontend: HTML5, CSS3, JavaScript
- Database: (by default SQLite, easy to connect to MongoDB)
- Admin: Django Admin
- Static Management: Django staticfiles
- Version Control: Git / GitHub

---

🚀 Getting Started

1. Clone the repo

   git clone https://github.com/yourusername/localpal.git
   cd localpal

2. Install dependencies

   pip install -r requirements.txt

3. Set up the database

   python manage.py makemigrations
   python manage.py migrate

4. Run the development server

   python manage.py runserver

   Then visit http://127.0.0.1:8000/

5. Create a superuser (for Django Admin)

   python manage.py createsuperuser

   Then log in at http://127.0.0.1:8000/admin/

---

📂 Project Structure

*localpal/
  +localapp/
    -static/localapp/        - CSS, images, JavaScript
    -templates/localapp/     - HTML templates
    -migrations/
    -admin.py
    -models.py
    -views.py
  +localpal/
    -settings.py
    -urls.py
    -wsgi.py
*manage.py

---

