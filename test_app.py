import requests
import pytest

def test_predict_integer_values():
    response = requests.get("http://127.0.0.1:5000/api/v1.0/predict?num1=3&num2=4")
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] == 1
    assert data["features"]["num1"] == 3.0
    assert data["features"]["num2"] == 4.0

def test_predict_float_values():
    response = requests.get("http://127.0.0.1:5000/api/v1.0/predict?num1=2.9&num2=2.9")
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] == 0
    assert data["features"]["num1"] == 2.9
    assert data["features"]["num2"] == 2.9

def test_predict_no_params():
    response = requests.get("http://127.0.0.1:5000/api/v1.0/predict")
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] == 0
    assert data["features"]["num1"] == 0.0
    assert data["features"]["num2"] == 0.0

def test_predict_invalid_input_string():
    response = requests.get("http://127.0.0.1:5000/api/v1.0/predict?num1=abc&num2=4")
    assert response.status_code == 400