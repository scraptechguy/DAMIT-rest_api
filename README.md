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
```python
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
├── data/shapes/      
│   ├── 47f96eff1d..         
│   └── d1b14688e2..         # Sample files (.obj)
│
├── requirements.txt         # Dependencies
├── run.py                   # Runs uvicorn
└── start_damit_rest_api.sh  # Runs the REST API
```

## Instructions to run

> Note: Make sure your database (MariaDB) is running and the credentials in app/config.py are correct.

#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Start the FastAPI development server from the run.py script and expose the local server to the internet with ngrok (requires ngrok to be installed)
```bash
./start_damit_rest_api.sh
```
> -> Visit the public URL printed by the script to access your API
