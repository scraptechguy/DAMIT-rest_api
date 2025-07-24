## This project is a Python-based REST API built with FastAPI that connects to a local MariaDB database to serve asteroid data for the DAMIT iOS native app.

<div align="center">
  <a href="https://github.com/scraptechguy/DAMIT-rest_api/actions">
    <img src="https://github.com/scraptechguy/DAMIT-rest_api/actions/workflows/python-package.yml/badge.svg">
  </a>
  <a href="https://github.com/scraptechguy/DAMIT-rest_api/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/scraptechguy/DAMIT-rest_api">
  </a>
  <a href="https://github.com/scraptechguy/DAMIT-rest_api/issues">
    <img src="https://img.shields.io/github/issues/scraptechguy/DAMIT-rest_api">
  </a>
  <a href="https://github.com/scraptechguy/DAMIT-rest_api/pulls">
    <img src="https://img.shields.io/github/issues-pr/scraptechguy/DAMIT-rest_api">
  </a>
</div>

## Project structure
```
DAMIT-rest_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # Entrypoint: FastAPI app
│   ├── db.py                # DB engine + session
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic data models (for API I/O)
│   ├── crud.py              # DB logic (Create, Read, Update, Delete)
│   └── config.py            # DB credentials
│
├── tests/
│   └── test_main.py         # Simulate HTTP requests
│
├── run.py                   # Runs uvicorn
└── requirements.txt         # Dependencies
```
