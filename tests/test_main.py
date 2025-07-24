from fastapi.testclient import TestClient
from app.main import app  # adjust import if needed

client = TestClient(app)

def test_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200
