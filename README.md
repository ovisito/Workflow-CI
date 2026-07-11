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
## 📁 Struktur Folder Proyek

Struktur proyek ini mengikuti ketentuan submission, dengan fokus utama pada folder `Workflow-CI`.

```bash
Workflow-CI/
├── .workflow/               # Konfigurasi GitHub Actions
│   └── ci.yml
├── MLProject/               # MLflow Project
│   ├── MLProject
│   ├── conda.yaml
│   └── modelling.py
├── namadataset_preprocessing/ # Data hasil preprocessing
│   ├── X_train.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   └── y_test.csv
├── Dockerfile               # Containerization
└── README.md
```
## 🚀 Cara Menjalankan Proyek

1.  **Clone Repository**
    ```bash
    git clone https://github.com/ovisito/Workflow-CI.git
    cd Workflow-CI
    ```

2.  **Jalankan Proyek MLflow**
    ```bash
    mlflow run MLProject/
    ```

3.  **Bangun Image Docker**
    ```bash
    docker build -t bank-marketing-mlops .
    ```

## ✅ Kriteria Submisi

- [x] Eksperimen model dengan MLflow Tracking
- [x] Workflow CI menggunakan GitHub Actions
- [x] Containerization dengan Docker
- [x] Sistem monitoring dan logging model

## 📄 Lisensi

Proyek ini dibuat sebagai bagian dari submisi kelas **Membangun Sistem Machine Learning** dan menggunakan lisensi **MIT License**.
