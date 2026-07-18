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

---
## Screenshots
<img width="1917" height="847" alt="image" src="https://github.com/user-attachments/assets/74ef94a6-7730-4bf1-bc0f-cd4cbf51837c" />
<img width="1919" height="820" alt="image" src="https://github.com/user-attachments/assets/d71ef356-f728-4250-9f78-1c02f05cb12a" />
<img width="1916" height="723" alt="image" src="https://github.com/user-attachments/assets/0fc38e6e-fc92-4700-9de6-2c9e018b7753" />
<img width="1917" height="820" alt="image" src="https://github.com/user-attachments/assets/40da3984-3ce2-4574-82b3-4268ce66ed1f" />

