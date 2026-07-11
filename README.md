# Workflow-CI - Bank Marketing MLOps

## 📌 Deskripsi Proyek

Proyek ini adalah implementasi **MLOps** untuk dataset Bank Marketing menggunakan:

- **MLflow** — untuk experiment tracking
- **GitHub Actions** — untuk CI/CD
- **Docker** — untuk containerization

## 📁 Struktur Folder

```
Workflow-CI/
├── .github/
│   └── workflows/
│       └── ci.yml
├── MLProject/
│   ├── conda.yaml
│   ├── MLproject
│   └── modelling.py
├── data/
│   └── bank_marketing.csv
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🚀 Cara Menjalankan

```bash
# Clone repository
git clone https://github.com/username/Workflow-CI.git
cd Workflow-CI

# Install dependencies
pip install -r requirements.txt

# Jalankan MLflow project
mlflow run MLProject/
```

## 🐳 Menjalankan dengan Docker

```bash
# Build image
docker build -t bank-marketing-mlops .

# Jalankan container
docker run -p 5000:5000 bank-marketing-mlops
```

## ⚙️ CI/CD Pipeline

Pipeline CI/CD dijalankan otomatis melalui **GitHub Actions** setiap kali ada `push` atau `pull_request` ke branch `main`, dengan tahapan:

1. Checkout repository
2. Setup environment (Python & dependencies)
3. Menjalankan MLflow project
4. Build & push Docker image (opsional)

## 📄 Lisensi

Proyek ini menggunakan lisensi **MIT License**.
