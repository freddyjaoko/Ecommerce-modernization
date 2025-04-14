# 🛒 Ecommerce Modernization

Took a dated application and turned it into a modern, containerized ecommerce application designed with best DevOps practices. This project includes full CI/CD automation, comprehensive testing, and seamless deployment to the cloud.

---

## 🚀 Features

- 🔧 **Modernized Ecommerce Backend**  
- 🐳 **Dockerized** application for consistent environments  
- ✅ **Automated Testing** with `pytest` and `coverage`  
- 🔍 **Code Quality Analysis** using **SonarQube**  
- 🔁 **CI/CD Pipeline** using **GitHub Actions**  
- 📦 **Docker Image Published** to DockerHub
- ☁️ **Deployment to Render** for public access
- 🔔 **Slack Notifications** for pipeline updates

---

## ⚙️ Tech Stack

- **Python**
- **Docker**
- **Pytest** for unit testing
- **Coverage** for test coverage reports
- **SonarQube** for static code analysis
- **GitHub Actions** for CI/CD
- **DockerHub** for container registry
- **Render** for deployment

---

## 🧪 Testing

Tests are run automatically as part of the CI pipeline using:

```bash
pytest --cov=.
```

### ✅ Coverage

Code coverage is enforced.

### 🔎 SonarQube

Static code analysis and quality checks are performed using SonarQube. Metrics like code smells, bugs, test coverage, and duplications are tracked.



---

## 🔄 CI/CD Pipeline (GitHub Actions)

The CI/CD pipeline is triggered on push and pull request events. It includes:


1. Install dependencies
2. Run lint and unit tests
3. Generate coverage reports
4. Run SonarQube analysis
5. Build and push Docker image to DockerHub
6. Deploy the latest image to Render

![Screenshot 2025-04-07 094852](https://github.com/user-attachments/assets/b569042b-0a32-438d-9569-6be44bc7e990)

---

## 🐳 Docker

### Build Image

```bash
docker build -t freddyjaoko/ecommerce-app .
```

### Run Locally

```bash
docker run -p 8000:8000 freddyjaoko/ecommerce-app

```

---

## 📦 DockerHub

Docker images are pushed automatically to:

📎 [DockerHub Repository](https://hub.docker.com/r/freddyjaoko/ecommerce-app)

---

## ☁️ Deployment

The latest Docker image is deployed to [Render](https://ecommerce-app-8vgr.onrender.com) via a deploy hook or Docker service setup.

📍 Deployed App: https://ecommerce-app-8vgr.onrender.com

---

📣 Slack Integration

Slack notifications are sent during each stage of the CI/CD pipeline to provide real-time visibility into:

🧪 Test results

📦 Build status

🚀 Deployment success/failure


![Screenshot 2025-04-06 203054](https://github.com/user-attachments/assets/2797c871-d5ec-43bf-ade3-77119eacef5c)
    

  ---


## 🛠️ Getting Started

Clone the repo:

```bash
git clone https://github.com/freddyjaoko/ecommerce-modernization.git
cd ecommerce-modernization
```

Run with Docker:

```bash
docker-compose up --build
```

Or run locally with Python:

```bash
pip install -r requirements.txt
python app.py
```

---

## 🧠 Future Enhancements

- Add API Gateway and authentication
- Migrate to Kubernetes
- Integrate with frontend (React, Vue, etc.)
- Performance monitoring with Prometheus + Grafana
