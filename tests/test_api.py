
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_valid_prediction():
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    )

    assert response.status_code == 200
    assert response.json()["predicted_species"] == "setosa"


def test_prediction_response_format():
    response = client.post(
        "/predict",
        json={
            "sepal_length": 6.0,
            "sepal_width": 3.0,
            "petal_length": 4.5,
            "petal_width": 1.5
        }
    )

    data = response.json()

    assert "predicted_species" in data
    assert "confidence" in data
    assert 0 <= data["confidence"] <= 1


def test_invalid_input():
    response = client.post(
        "/predict",
        json={"sepal_length": 5.1}
    )

    assert response.status_code == 422