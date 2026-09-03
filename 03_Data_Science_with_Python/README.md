# Track 3: Virtual Data Science with Python Apprentice

This directory contains the production-grade Python machine learning pipelines, time-series feature engineering modules, and executive capstone deliverables developed for agricultural market forecasting.

---

## 📌 Deliverables & Core Modules

* **Week 1: Python Architecture & Ingestion Strategy**
  - Architecture plan for multi-source data ingestion, schema validation, and fail-safe monitoring.
  - Artifact: `Week1_Python_Data_Science_Architecture_Plan.docx`

* **Week 2: Feature Engineering & Temporal Extraction**
  - Leakage-free feature construction: 7-day rolling SMAs, autoregressive price lags, and log-transformed arrival volumes.
  - Artifact: `Week2_Automated_EDA_Feature_Engineering_Python.docx`

* **Week 3: ML Pipeline Design & Validation Strategy**
  - Chronological walk-forward split design to prevent future lookahead leakage in market pricing models.
  - Artifact: `Week3_Predictive_Pipeline_Design_Python.docx`

* **Week 4: Machine Learning Model Development & Benchmarking**
  - Trained and tuned Random Forest Classifiers against baseline Logistic Regression models.
  - **Diagnostic Metrics:** 76.8% Accuracy | 0.78 Precision (Breakout) | 0.835 ROC-AUC.
  - Artifact: `Week4_ML_Model_Development_Evaluation.docx`

* **Week 5: Comprehensive Data Science Capstone Report**
  - Complete agribusiness strategic framework: dynamic procurement rules, inventory buffer triggers, and ROI models.
  - Artifact: `Week5_Comprehensive_Data_Science_Capstone_Report.docx`

---

## 🛠️ Production Python Pipeline

* **Model Pipeline Script:** [`scripts/ml_model_pipeline.py`](scripts/ml_model_pipeline.py)
  - Features end-to-end data ingestion, temporal ordering, StandardScaler transformations, Random Forest training, and classification diagnostics.
