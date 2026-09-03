# Track 2: Virtual Data Science with R Apprentice

This track focuses on econometric modeling, statistical data wrangling, and predictive price regime classification using R on national wholesale agricultural market data (Agmarknet).

---

## 📌 Deliverables & Analytical Breakdown

* **Week 1: Project Planning & Econometric Research Design**
  - Operational research plan modeling the Cobweb Phenomenon and localized agricultural price inelasticity.
  - Artifact: `Week1_Project_Planning_Strategy_Development_R.docx`

* **Week 2: Exploratory Data Analysis & Statistical Visualizations**
  - Ingested 48,520 transaction rows across Northern Indian Mandis.
  - Fitted Generalized Additive Models (GAM) identifying the 200-tonne supply saturation tipping point.
  - Artifact: `Week2_Exploratory_Data_Analysis_Visualization_R.docx`

* **Week 3: Data Wrangling, Imputation & Feature Engineering**
  - Implemented localized district-commodity median imputation and non-parametric IQR outlier mitigations.
  - Engineered logarithmic volume transforms and normalized intra-day spreads.
  - Artifact: `Week3_Data_Wrangling_Preprocessing_R.docx`

* **Week 4: Supervised Model Building & Validation**
  - Chronological 80/20 out-of-sample evaluation benchmarking Logistic Regression vs. Random Forest.
  - **Random Forest Performance:** 77.4% Directional Accuracy | 0.841 ROC-AUC.
  - Artifact: `Week4_Model_Building_Predictive_Analysis_R.docx`

* **Week 5: Final Capstone Synthesis & Strategic Reporting**
  - Strategic roadmaps for dynamic inventory buffering and cold-storage infrastructure prioritization.
  - Artifact: `Week5_Reporting_Insights_Presentation_R.docx`

---

## 🛠️ Executable R Scripts

* **EDA & Visualization Pipeline:** [`scripts/eda_visualization.R`](scripts/eda_visualization.R)
* **Wrangling & Imputation Engine:** [`scripts/data_wrangling_pipeline.R`](scripts/data_wrangling_pipeline.R)
* **Predictive Regime Classifier:** [`scripts/predictive_modeling_r.R`](scripts/predictive_modeling_r.R)
