# Assignhut

A Django web application project (uses SQLite by default) with templates and static assets.

> Repo structure includes: `manage.py`, `db.sqlite3`, `templates/`, `static/`, `user/` app, and `MyProject/` Django project folder. :contentReference[oaicite:1]{index=1}

---

## Tech Stack
- Backend: Python + Django
- Database: SQLite (`db.sqlite3`)
- Frontend: Django Templates + Static files (CSS/JS/images)

---

## Project Structure

Assignhut/
├─ MyProject/ # Django project settings (project config)
├─ user/ # Django app (user-related module)
├─ templates/ # HTML templates
├─ static/ # CSS/JS/images
├─ db.sqlite3 # SQLite database (local)
├─ manage.py # Django entry point


---

## Getting Started (Local Setup)

### 1) Clone the repository
```bash
git clone https://github.com/vaishnavisingh20/Assignhut.git
cd Assignhut
```
2) Create & activate virtual environment

Windows (PowerShell)
```bash
python -m venv venv
.\venv\Scripts\Activate
```

macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
3) Install dependencies
   
4) Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
5) Start the server
```bash
python manage.py runserver
```

  Open:
  
  http://127.0.0.1:8000/

Admin Setup (Optional)

Create an admin user:
```bash
python manage.py createsuperuser
```

Then visit:
http://127.0.0.1:8000/admin
