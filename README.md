# Credit Card Default Analysis

This project analyzes the [UCI Credit Card Default Dataset](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients) to explore customer default payments in Taiwan. The goal is to learn and apply various data analysis and anomaly detection techniques.

## Project Structure

- `main.ipynb` — Main Jupyter notebook for data analysis, feature engineering, and anomaly detection.
- `input/` — Contains the dataset file (`default of credit card clients.xls`).
- `utils/` — Utility functions used in the notebook.
- `README.md` — Project documentation.
- `pyproject.toml`, `uv.lock` — Project dependencies and environment files.

## Steps Covered

1. **Data Loading & Cleaning**  
   - Reads the dataset and cleans column names.
   - Handles data types and missing values.

2. **Exploratory Data Analysis (EDA)**  
   - Visualizes distributions of demographic, bill, and payment features.
   - Examines target variable and categorical features.

3. **Feature Engineering**  
   - Creates new features (e.g., payment delays, bill/payment trends, ratios).
   - Encodes categorical variables and normalizes features.

4. **Train/Validation/Test Split**  
   - Splits the data for model evaluation.

5. **Anomaly Detection Methods**  
   - Z-score, IQR, Mahalanobis distance, PCA, Isolation Forest, One-Class SVM, Local Outlier Factor, DBSCAN.

## Requirements

- Python 3.8+
- Jupyter Notebook
- pandas, numpy, matplotlib, seaborn, scikit-learn, scipy

Install dependencies using:

```sh
uv sync
```
or use the environment manager of your choice.

## Usage

1. Open `main.ipynb` in Jupyter Notebook or VS Code.
2. Run the notebook cells to follow the analysis.

## Purpose

This project is for learning and practicing data analysis, feature engineering, and anomaly detection techniques on a real-world dataset.