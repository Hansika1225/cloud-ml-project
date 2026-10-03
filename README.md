# Cloud-Based ML Prediction API

A containerized machine learning prediction API built using **Python, Scikit-learn, FastAPI, Docker, GitHub Actions, and Render**.

The project demonstrates a simple **client-server architecture** in which a client sends input data to a REST API, the API uses a trained machine learning model to generate a prediction, and the result is returned as JSON.

The application is deployed on **Render Cloud** and accessed through a public HTTPS API endpoint.

---

## 1. Project Overview

This project uses the **Iris dataset** to train a Logistic Regression machine learning model.

The trained model is integrated into a FastAPI application that provides a `/predict` endpoint.

A client can send the four measurements of an Iris flower:

- Sepal length
- Sepal width
- Petal length
- Petal width

The API returns:

- Predicted flower species
- Prediction confidence

The application is packaged inside a Docker container, tested automatically using GitHub Actions, and deployed to **Render Cloud** as a Docker-based Web Service.

---

## 2. Problem Statement

Machine learning models are useful only when they can be integrated into applications and made accessible to users or other software systems.

The objective of this project is to demonstrate how a trained ML model can be:

1. Trained using a dataset
2. Saved as a reusable model artifact
3. Exposed through a REST API
4. Containerized using Docker
5. Tested automatically using CI
6. Deployed to a cloud platform using Render

---

## 3. Architecture

```text
                    Client
                      |
                      | HTTPS Request
                      v
              +---------------+
              | Render Cloud  |
              |   Platform    |
              +-------+-------+
                      |
                      v
              +---------------+
              | Docker        |
              | Container     |
              +-------+-------+
                      |
                      v
              +---------------+
              |   FastAPI     |
              |   REST API    |
              +-------+-------+
                      |
                      v
              +---------------+
              | ML Model      |
              | Logistic      |
              | Regression    |
              +-------+-------+
                      |
                      | Prediction
                      v
              +---------------+
              | JSON Response |
              +---------------+
```

### Development and CI/CD Flow
```
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +----> Install Dependencies
    |
    +----> Run Automated Tests
    |
    +----> Build Docker Image
    |
    v
Render Cloud
    |
    v
Docker Container
    |
    v
Public HTTPS API
```
---

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application and ML development |
| Scikit-learn | Machine learning model |
| FastAPI | REST API |
| Pydantic | API input validation |
| Joblib | Saving/loading the trained model |
| Docker | Containerization |
| Pytest | Automated testing |
| GitHub Actions | Continuous Integration |
| GitHub | Source code management |
| Render | Cloud deployment and hosting |

---

## 5. Machine Learning Model

The project uses the built-in **Iris dataset** provided by Scikit-learn.

The model pipeline consists of:

```text
Iris Dataset
     |
     v
Train/Test Split
     |
     v
StandardScaler
     |
     v
Logistic Regression
     |
     v
Trained Model
     |
     v
iris_model.pkl
```

The model predicts one of three Iris species:

- Setosa
- Versicolor
- Virginica

The trained model, target names, and feature information are stored in:

```text
iris_model.pkl
```

---

## 6. API

The FastAPI application provides the following endpoints.

### Home Endpoint

```http
GET /
```

Returns a message confirming that the API is running.

Example response:

```json
{
  "message": "Iris ML Prediction API is running!"
}
```

---

### Prediction Endpoint

```http
POST /predict
```

The endpoint accepts four numerical features.

Example request:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Example response:

```json
{
  "predicted_species": "setosa",
  "confidence": 0.983
}
```

---

## 7. Running the Project Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/Hansika1225/cloud-ml-project.git
cd cloud-ml-project
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Step 5: Open Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test the `/predict` endpoint.

---

## 8. Running with Docker

The application is containerized using Docker.

### Build the Docker image

```bash
docker build -t iris-ml-api .
```

### Run the container

```bash
docker run -d -p 8000:8000 --name iris-api iris-ml-api
```

The API will then be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

To stop the container:

```bash
docker stop iris-api
```

To remove the container:

```bash
docker rm iris-api
```

---

## 9. Testing

The project contains four automated tests.

The tests verify:

1. Home endpoint functionality
2. Valid ML prediction
3. Prediction response format
4. Invalid input handling

Run the tests using:

```bash
python -m pytest -v
```

Expected result:

```text
4 passed
```

---

## 10. Continuous Integration

GitHub Actions is used to automatically test the project whenever changes are pushed or a pull request is created.

The CI pipeline performs the following steps:

```text
Checkout Code
      |
      v
Set Up Python
      |
      v
Install Dependencies
      |
      v
Run Pytest
      |
      v
Build Docker Image
```

The workflow is located at:

```text
.github/workflows/ci.yml
```

The `main` branch is protected so that the required CI check must pass before changes can be merged through a pull request.

---

## 11. Cloud Deployment

The application is containerized using Docker and deployed to **Render Cloud** as a Web Service.

### Cloud Platform

## Render

Render provides the cloud environment in which the Dockerized FastAPI application runs and is made accessible through a public HTTPS endpoint.

### Deployment Architecture

```text
Client
  |
  | HTTPS Request
  v
Render Cloud Platform
  |
  v
Docker Container
  |
  v
FastAPI
  |
  v
Iris ML Model
  |
  v
JSON Prediction
```

### Deployed Application

**Cloud Platform:** Render

**Live URL:**  
[https://iris-ml-api-rl5l.onrender.com/?utm_source=chatgpt.com](https://iris-ml-api-rl5l.onrender.com)

**Swagger API:**  
[https://iris-ml-api-rl5l.onrender.com/docs](https://iris-ml-api-rl5l.onrender.com/docs)

---

## 12. Project Features

- Machine learning model training
- REST API for ML predictions
- Input validation using Pydantic
- Docker containerization
- Automated testing using Pytest
- GitHub Actions CI pipeline
- Protected main branch
- Cloud deployment
- Interactive Swagger API documentation

---

## 13. Project Structure

```text
cloud-ml-project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── tests/
│   └── test_api.py
│
├── main.py
├── train_model.py
├── iris_model.pkl
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 14. High-Level Working

The complete workflow of the project is:

```text
1. Iris dataset is loaded
          ↓
2. Logistic Regression model is trained
          ↓
3. Trained model is saved as iris_model.pkl
          ↓
4. FastAPI loads the saved model
          ↓
5. Client sends flower measurements
          ↓
6. FastAPI validates the input
          ↓
7. ML model generates a prediction
          ↓
8. API returns prediction + confidence
          ↓
9. Application runs inside Docker
          ↓
10. Docker container is deployed to the cloud
```

---

## 15. Future Improvements

Possible future improvements include:

- Adding a web-based frontend
- Adding authentication
- Supporting additional ML models
- Adding model monitoring
- Adding logging and performance monitoring
- Automating cloud deployment through CI/CD
- Adding more datasets and prediction endpoints

---

## 16. Conclusion

This project demonstrates the complete process of taking a small machine learning model and making it accessible as a cloud-based API.

It combines:

**Machine Learning + REST API + Docker + Automated Testing + CI + Cloud Deployment**

The project provides a practical example of how ML models can be integrated into deployable software applications.
