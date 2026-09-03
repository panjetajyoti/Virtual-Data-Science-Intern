"""
Generic Exploratory Data Analysis (EDA) & Visualization Engine
Designed for Week 2: Adaptable across tabular numerical and categorical datasets.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AutomatedEDAFramework:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()
        self.num_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        self.cat_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()

    def audit_data_quality(self) -> pd.DataFrame:
        """Returns structural audit: missing values, unique counts, and data types."""
        audit_dict = {
            'Data_Type': self.df.dtypes,
            'Missing_Count': self.df.isnull().sum(),
            'Missing_Percentage': (self.df.isnull().sum() / len(self.df)) * 100,
            'Unique_Values': self.df.nunique()
        }
        audit_df = pd.DataFrame(audit_dict)
        return audit_df.sort_values(by='Missing_Percentage', ascending=False)

    def detect_outliers_iqr(self, col: str) -> tuple:
        """Calculates IQR-based non-parametric outlier boundaries."""
        if col not in self.num_cols:
            raise ValueError(f"{col} is not a continuous numerical feature.")
        q1 = self.df[col].quantile(0.25)
        q3 = self.df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)]
        return lower_bound, upper_bound, len(outliers)

    def generate_correlation_matrix(self, save_path: str = None):
        """Generates a filtered correlation matrix for numerical features."""
        if len(self.num_cols) < 2:
            print("Insufficient numerical variables for correlation analysis.")
            return
        plt.figure(figsize=(10, 8))
        corr = self.df[self.num_cols].corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))
        sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="vlag", vmin=-1, vmax=1)
        plt.title("Filtered Upper-Triangle Feature Correlation Matrix", fontsize=12, fontweight='bold')
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300)
        plt.show()

if __name__ == "__main__":
    # Smoke-test execution with mock tabular features
    np.random.seed(42)
    mock_data = pd.DataFrame({
        'Entity_ID': [f"ID_{i}" for i in range(100)],
        'Numerical_A': np.random.normal(50, 15, 100),
        'Numerical_B': np.random.exponential(5, 100),
        'Category_Segment': np.random.choice(['Low', 'Medium', 'High'], 100)
    })
    eda = AutomatedEDAFramework(mock_data)
    print("Quality Audit Summary:")
    print(eda.audit_data_quality())
