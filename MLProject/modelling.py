# modelling.py - Untuk Workflow CI

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import mlflow
import mlflow.sklearn
import os
import argparse   # <-- Tambahkan ini

# 1. Setup argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--data_path", type=str, default="namadataset_preprocessing",
                    help="Path ke folder dataset yang sudah dipreprocess")
args = parser.parse_args()

# 2. Gunakan data_path untuk membangun path file
data_path = args.data_path

print("📂 Loading data from:", data_path)
X_train = pd.read_csv(os.path.join(data_path, "X_train.csv"))
X_test  = pd.read_csv(os.path.join(data_path, "X_test.csv"))
y_train = pd.read_csv(os.path.join(data_path, "y_train.csv")).values.ravel()
y_test  = pd.read_csv(os.path.join(data_path, "y_test.csv")).values.ravel()

print("💪 Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {accuracy:.4f}")
print(classification_report(y_test, y_pred))

with mlflow.start_run(run_name="CI_Run"):
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "random_forest_model")
    print("🎉 MLflow logging selesai!")
