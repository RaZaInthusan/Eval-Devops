from fastapi.testclient import TestClient
from app.mini_groq import app

client = TestClient(app)

def test_get_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
