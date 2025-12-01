# AI Job Agent Django Project (Full)

This repository contains a full starter Django project implementing an agent-based job assistant.

## Quick start

1. Create virtualenv and install:
   pip install -r requirements.txt

2. (Optional) Use MySQL:
   - Configure .env and set USE_MYSQL=1
   - Ensure mysqlclient and MySQL server are installed

3. Run migrations:
   python manage.py migrate

4. Create superuser:
   python manage.py createsuperuser

5. Run server:
   python manage.py runserver

## API endpoints

- GET /api/jobs/ - list jobs
- POST /api/agent/ - agent endpoint (see README for payloads)
- POST /api/jobs/create/ - create job (admin or programmatic)

Payload example for agent:
{
  "type": "job",
  "input": "python,django"
}

For apply:
{
  "type": "apply",
  "input": {"job_id": 1}
}
