# Cafe Menu — Backend

Django + DRF backend for a QR-based cafe menu system.

## Stack
- Django 6 + Django REST Framework
- PostgreSQL
- Docker Compose

## Run the project

1. Copy the environment file and fill in values:
```bash
   cp .env.example .env
```

2. Build and start the containers:
```bash
   docker compose up --build
```

3. In a new terminal, apply migrations:
```bash
   docker compose exec web python manage.py migrate
```

4. Create an admin user:
```bash
   docker compose exec web python manage.py createsuperuser
```

5. Visit:
   - App: http://localhost:8000
   - Admin: http://localhost:8000/admin

## Project structure
- `config/` — Django project settings
- `menu/` — menu app (Category, MenuItem, CafeSettings models)