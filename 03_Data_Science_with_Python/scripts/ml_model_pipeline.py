"""
End-to-End Supervised Machine Learning Pipeline in Python
Track: Virtual Data Science with Python Apprentice (Weeks 4 & 5)
Focus: Price Regime Classification using Random Forest and Logistic Regression
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

def run_ml_pipeline(filepath: str):
    # 1. Ingestion and Chronological Ordering
    df = pd.read_csv(filepath)
    df['Arrival_Date'] = pd.to_datetime(df['Arrival_Date'])
    df = df.sort_values(by=['Market', 'Commodity', 'Arrival_Date']).reset_index(drop=True)

    # 2. Binary Target Creation (1: Price Increase Tomorrow, 0: Down/Flat)
    df['Target_Direction'] = (
        df.groupby(['Market', 'Commodity'])['Modal_Price'].shift(-1) > df['Modal_Price']
    ).astype(int)

    # 3. Leakage-Free Feature Engineering
    df['Price_Lag1'] = df.groupby(['Market', 'Commodity'])['Modal_Price'].shift(1)
    df['Arrivals_Log'] = np.log1p(df['Arrivals_Tonnes'])
    df['Price_SMA_7'] = df.groupby(['Market', 'Commodity'])['Modal_Price'].transform(
        lambda x: x.rolling(7).mean()
    )
    df['Volatility_Spread'] = (df['Max_Price'] - df['Min_Price']) / df['Modal_Price']

    # Clean rows with shift-induced NaNs
    clean_df = df.dropna().copy()

    features = ['Price_Lag1', 'Arrivals_Log', 'Price_SMA_7', 'Volatility_Spread']
    X = clean_df[features]
    y = clean_df['Target_Direction']

    # 4. Chronological 80/20 Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, shuffle=False)

    # Feature Standardization
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 5. Model Training & Evaluation
    models = {
        "Logistic Regression": LogisticRegression(random_state=42, C=1.0),
        "Random Forest Classifier": RandomForestClassifier(
            n_estimators=150, max_depth=6, min_samples_leaf=4, random_state=42
        )
    }

    results = {}
    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        y_prob = model.predict_proba(X_test_scaled)[:, 1]
        
        auc = roc_auc_score(y_test, y_prob)
        print(f"\n--- {name} Performance ---")
        print(classification_report(y_test, y_pred, digits=3))
        print(f"ROC-AUC: {auc:.3f}")
        results[name] = {"model": model, "auc": auc}

    return results

if __name__ == "__main__":
    print("ML Pipeline Architecture loaded successfully.")
