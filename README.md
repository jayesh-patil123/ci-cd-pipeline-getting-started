# ci-cd-pipeline-getting-started
# 🚀 CI/CD Pipeline - Getting Started

Welcome to the **CI/CD Pipeline - Getting Started** project! This repository demonstrates how to set up a **Continuous Integration (CI) and Continuous Deployment (CD)** pipeline using **GitHub Actions**.

## 📌 Project Overview
This project includes:
- A **Python application** with basic mathematical functions.
- A **test suite** using `pytest`.
- A **GitHub Actions workflow** (`.github/workflows/python-app.yml`) for **automated testing and deployment**.

## 🏗️ CI/CD Pipeline Workflow
### 🔹 1. Build & Test (CI)
Whenever code is pushed to the `main` branch or a pull request is created, the following steps are triggered:

✅ **Checkout Code** - Fetches the latest code from GitHub.  
✅ **Set up Python** - Installs Python 3.10.  
✅ **Install Dependencies** - Installs required dependencies.  
✅ **Linting with flake8** - Checks code quality and style.  
✅ **Run Tests with pytest** - Ensures the code works correctly.  

### 🔹 2. Deployment (CD)
After a successful build, if the push is on the `main` branch, the deployment process starts:

🚀 **Deploy to Production** - A placeholder command for actual deployment.

## 🛠️ Project Structure
```
ci-cd-pipeline-getting-started/
│── .github/workflows/python-app.yml   # CI/CD Pipeline workflow
│── src/
│   ├── main.py                        # Core Python functions
│── tests/
│   ├── test_main.py                    # Unit tests
│── .gitignore
│── README.md                          # Documentation
│── requirements.txt                    # Dependencies
```

## 📝 GitHub Actions Workflow (`.github/workflows/python-app.yml`)
```yaml
name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        flake8 . --exclude=venv --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 . --exclude=venv --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest

  deploy:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
      - name: Deploy to Production
        run: |
          echo "Starting deployment..."
```

## 📂 Source Code (`src/main.py`)
```python
def add(a, b):
    return a + b

def substract(a, b): # new function
    return a - b
```

## 🧪 Test Cases (`tests/test_main.py`)
```python
from src.main import add, substract

def test_add_function():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(5, 5) == 10

def test_substract_function():
    assert substract(5, 3) == 2
    assert substract(0, 0) == 0
    assert substract(10, 5) == 5
```

## 📜 Dependencies (`requirements.txt`)
```txt
pytest==8.3.3
```

## 🎯 How to Run Locally
```bash
# Clone the repository
$ git clone https://github.com/your-username/ci-cd-pipeline-getting-started.git

# Navigate to the project directory
$ cd ci-cd-pipeline-getting-started

# Create a virtual environment (optional)
$ python -m venv venv
$ source venv/bin/activate   # On Windows use: venv\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt

# Run tests
$ pytest
```

## 🎉 Conclusion
This project sets up an automated CI/CD pipeline with **GitHub Actions** to ensure high code quality and deployment readiness. The CI/CD workflow automatically tests and deploys the code, making development efficient and reliable.

🔹 **CI/CD Benefits:** Automated testing, better code quality, faster deployments! 🚀

---

Made with ❤️ by **Jayesh Patil**
