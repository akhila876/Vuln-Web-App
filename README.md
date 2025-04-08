# Vulnerable Web Application 

This is a **basic Django-based web application** developed from scratch without any validations, intended **strictly for learning and experimenting with security vulnerabilities**. It includes user authentication, image uploads, personal galleries, post creation, and account management features.

---

## Features Implemented

- **User Registration**: New users can register (no validation on inputs).
- **User Login**: Existing users can log in.
- **Profile Page**: Displays user info like `username` and `email`.
- **Image Upload**: Users can upload image files.
- **User Gallery**: Users can only see images they uploaded.
- **Post Creation**: Users can post text content.
- **Password Change**: Logged-in users can change their password.
- **Session Handling**: Basic session-based login system.
- **No Design Focus**: Prioritizes functionality over UI.

---

##  Technologies Used

- Python 3.11.9
- Django 5.2
- SQLite (default Django DB)
- HTML/CSS (basic, minimal styling)

---

##  Project Structure

WEB APPLICATION/                     # Root project directory
│
├── app/                        # Django app
│   ├── migrations/             # Auto-created DB migration files
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                # Form classes
│   ├── models.py               # Database models
│   ├── urls.py                 # App-specific URLs
│   └── views.py                # App logic
│
├── media/ 
│    └── uploads                 # Uploaded files (images)
│
├── static/
│   └── style.css  
│
├── templates/              # HTML templates
│   ├── base.html
│   ├── change_password.html
│   ├── create_post.html
│   ├── gallery.html
│   ├── index.html
│   ├── login.html
│   ├── profile.html
│   └── register.html
│
├── vuln_webapp/                # Django project config directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py             # Project-wide settings
│   ├── urls.py                 # Main URLs (includes app.urls)
│   └── wsgi.py
│
├── db.sqlite3                  # SQLite database file
├── manage.py                   # Django's command-line utility
├── README.md                   # Setup and project overview
└── requirements.txt            # Dependencies 


---

##  How to Run Locally

Follow the steps below to set it up on your system.

### 1.  Clone the Project

git clone https://github.com/yourusername/vuln_webapp.git
cd vuln_webapp

### 2.  Create Virtual Environment

python -m venv venv

venv\Scripts\activate    # Windows
# or
source venv/bin/activate # Linux/Mac

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

### 5. Create Superuser (For Admin Access)

python manage.py createsuperuser

### 6. Run the Development Server

python manage.py runserver

* Access the app at: http://127.0.0.1:8000/

* Admin Panel (if superuser created): http://127.0.0.1:8000/admin/

---