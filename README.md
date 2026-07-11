# Membangun Sistem Machine Learning

**Nama Siswa  :** Muhammad Aiyub
**Tugas       :** Submisi Final — Membangun Sistem Machine Learning

---

## 📌 Deskripsi Proyek

Proyek ini merupakan submisi final dari kelas **Membangun Sistem Machine Learning**, yang mencakup keseluruhan alur MLOps mulai dari eksperimen model, tracking, hingga deployment sistem machine learning secara end-to-end.

## 🎯 Tujuan

- Membangun pipeline machine learning yang terstruktur dan dapat direproduksi
- Melakukan tracking eksperimen menggunakan **MLflow**
- Mengimplementasikan CI/CD untuk proses training dan deployment model
- Melakukan containerization sistem menggunakan **Docker**
- Menyediakan sistem monitoring untuk model yang telah di-deploy

## 🛠️ Tools & Teknologi

| Kategori             | Tools/Teknologi      |
|-----------------------|-----------------------|
| Experiment Tracking   | MLflow                |
| CI/CD                 | GitHub Actions        |
| Containerization      | Docker                |
| Monitoring            | Prometheus & Grafana  |
| Bahasa Pemrograman    | Python                |

## 📁 Struktur Folder

```
Submission/
├── MLProject/
│   ├── conda.yaml
│   ├── MLproject
│   └── modelling.py
├── Workflow-CI/
│   ├── .github/workflows/
│   ├── MLProject/
│   └── Dockerfile
├── Monitoring dan Logging/
│   ├── prometheus.yml
│   ├── inference.py
│   └── dashboard/
├── data/
├── requirements.txt
└── README.md
```

## 🚀 Cara Menjalankan

```bash
# Clone repository
git clone https://github.com/username/submission-mlops.git
cd submission-mlops

# Install dependencies
pip install -r requirements.txt

# Jalankan MLflow project
mlflow run MLProject/
```

## ✅ Kriteria Submisi

- [x] Eksperimen model dengan MLflow Tracking
- [x] Workflow CI menggunakan GitHub Actions
- [x] Containerization dengan Docker
- [x] Sistem monitoring dan logging model

## 📄 Lisensi

Proyek ini dibuat sebagai bagian dari submisi kelas **Membangun Sistem Machine Learning** dan menggunakan lisensi **MIT License**.
