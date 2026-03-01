# 🚀 Dockerized System Monitoring Tool (Python + Docker)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

## 📌 Project Overview

This project is a real-time CLI-based System Monitoring Tool built using Python and containerized using Docker.

It monitors and displays important system metrics such as:

- CPU Usage
- Memory Usage
- Disk Usage
- System Uptime
- Top 5 Running Processes

The application can run both locally and inside a Docker container.

This project demonstrates a complete end-to-end DevOps workflow:

Development → Testing → Containerization → Documentation → Version Control

---

## 🎯 Problem Statement

Developers and system administrators need a lightweight terminal-based tool to quickly monitor system health.

This project provides a clean CLI dashboard that refreshes automatically every 5 seconds and alerts when resource usage becomes high.

---

## 🛠 Technologies Used

- Python 3
- psutil (System Monitoring Library)
- Docker
- Git & GitHub
- VS Code

---

## 📂 Project Structure
```
system-monitor/
│
├── monitor.py
├── requirements.txt
├── Dockerfile
├── README.md
└── screenshots/
    └── output.png
```
---

## ⚙️ Features

✔ Real-time monitoring  
✔ Automatic refresh every 5 seconds  
✔ High CPU usage alert  
✔ High memory usage alert  
✔ Clean CLI dashboard  
✔ Safe exit handling (CTRL + C)  
✔ Docker container support  

---

## 🧠 How It Works

- Uses the `psutil` library to collect system statistics.
- Runs inside a loop to refresh data every 5 seconds.
- Clears the terminal screen to simulate a live dashboard.
- Displays top 5 CPU-consuming processes.
- Can run locally or inside a Docker container.

---

## ▶️ Run Locally (Without Docker)

### 1️⃣ Install Dependency
```
pip install psutil
```

### 2️⃣ Run the Application
```
python monitor.py
```
Stop the application safely using:
```
CTRL + C
```
---

## 🐳 Run Using Docker

### 1️⃣ Build Docker Image
```
docker build -t system-monitor .
```
### 2️⃣ Run Container
```
docker run -it system-monitor
```
Stop container using:
```
CTRL + C
```
---

## 🖥 Sample Output

The dashboard displays:

- CPU Usage
- Memory Usage
- Disk Usage
- System Uptime
- Top 5 Running Processes

### 📷 Application Screenshot

![System Monitor Output](screenshots/output.png)

---

## 🚀 DevOps Concepts Demonstrated

- Python system-level scripting
- Containerization using Docker
- Writing Dockerfile
- Dependency management using requirements.txt
- Building Docker images
- Running interactive containers
- Clean exit handling
- Git version control
- Professional documentation practices

---

## 📈 What I Learned

- How system metrics are collected using psutil
- How Docker isolates applications from host system
- Difference between host monitoring and container monitoring
- How to structure production-ready projects
- End-to-end development workflow

---

## 👨‍💻 Author

Gumparlapati Eswar

---

⭐ If you found this project useful, feel free to star the repository.