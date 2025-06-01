<<<<<<< HEAD
# Legacy Heights University Web Application

A Django-based web application for managing university activities, programs, staff, students, and more.

## Features

- User registration and authentication (students and staff)
- Program and course listings
- Activities and events gallery
- Staff directory and profiles
- Student mark sheet viewing
- Online payment section
- About, Terms, and Privacy pages
- Responsive design with light/dark theme toggle

## Project Structure

project/
├── .gitignore
├── LICENSE
├── README.md
├── requirement.txt
├── scaffold.py
└── final_project/
    ├── db.sqlite3
    ├── manage.py
    ├── about_us/
    ├── accounts/
    ├── activities/
    ├── core/
    ├── marksheet/
    ├── payment/
    ├── programs/
    ├── staff/
    ├── staff_photos/
    ├── staticfiles/
    └── students/

- **about_us/**: About, Terms, and Privacy pages
- **accounts/**: User registration, login, and account management
- **activities/**: Campus activities and gallery
- **core/**: Base templates and static files
- **marksheet/**: Student mark sheet viewing
- **payment/**: Payment section
- **programs/**: Program and course listings
- **staff/**: Staff directory
- **students/**: Student-related features

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
   sh
   git clone https://github.com/yourusername/legacy-heights-university.git
   cd legacy-heights-university/project
   

2. **Install dependencies:**
   sh
   pip install -r requirement.txt
   

3. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill in your secret key and settings.

4. **Apply migrations:**
   sh
   python final_project/manage.py migrate
   

5. **Create a superuser (optional, for admin access):**
   sh
   python final_project/manage.py createsuperuser
   

6. **Run the development server:**
   sh
   python final_project/manage.py runserver
   

7. **Access the app:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Environment Variables

Create a `.env` file in the project root. Example:

SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=sqlite:///final_project/db.sqlite3


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

- Built with [Django](https://www.djangoproject.com/)
- Icons and some static assets from [Font Awesome](https://fontawesome.com/)
- UI Design by JAWNCHAW HTANG NAM & CHRISTY RUTH
- Backend configuring and all by LAITEI
- 
=======
# Legacy-Heights-University
The Final Project by ICFAI University BCA Final Students Group 3.
>>>>>>> db221299fb62c5c9dbc66977a567c65d354412c2
