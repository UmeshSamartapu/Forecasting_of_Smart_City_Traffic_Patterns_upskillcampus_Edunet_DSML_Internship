# 🚦 Traffic Pattern Forecasting Report for Smart City Initiative

## 📌 1. Problem Definition

- **Business Goal:** Predict hourly vehicle counts at 4 city junctions to improve traffic management and infrastructure planning.
- **Problem Type:** Time-series regression
- **Success Metrics:**
  - **Primary:** Mean Absolute Error (MAE) < 15 vehicles
  - **Secondary:** R² Score > 0.85 on test data

---

## 📊 2. Data Collection

- **Source:** Historical traffic data (2015–2017) from city sensors
- **Files:**
  - `TrainDataSet.csv` (28,681 records)
  - `TestDataSet.csv` (10,088 records)
- **Tools:** `pandas` for data ingestion & analysis

---

## 🧹 3. Data Preprocessing

- **Operations:**
  - Auto-detect DateTime format
  - Checked for missing values – none found
  - Applied Winsorization (top/bottom 1%) to vehicle counts
  - Extracted temporal features: `Hour`, `DayOfWeek`, `IsWeekend`, `Month`
  - Performed 80-20 stratified validation split by junction
- **Libraries:** `pandas`, `numpy`, `scikit-learn`

---

## 📈 4. Exploratory Data Analysis (EDA)

- **Key Insights:**
  - Peak hours: 8 AM & 6 PM
  - Junction 1 handles ~38% of city traffic
  - Weekend traffic ~22% lower than weekdays
  - December traffic ~15% higher (holiday shopping)
- **Tools:** `matplotlib`, `seaborn`

---

## 🏗️ 5. Feature Engineering

- **New Features:**
  - Sin/Cos encoding for `Hour` and `Month`
  - 3-hour rolling average for traffic momentum
  - Public holiday flag
- **Feature Selection:**
  - Recursive Feature Elimination selected 7 of 12 features
- **Libraries:** `sklearn.feature_selection`, `pandas`

---

## 🤖 6. Model Selection

- **Algorithms Considered:**
  - ✅ **XGBoost Regressor** (Selected)
  - LSTM Neural Network
  - Prophet Time Series Model
- **Selection Rationale:**
  - MAE = 9.2 with good inference speed
  - Handles missing values & mixed data types
- **Libraries:** `XGBoost`, `scikit-learn`

---

## 🧠 7. Model Training

- **Settings:**
  - Early stopping rounds: 50
  - TimeSeriesSplit: 5 folds
- **Best Params:**
  ```python
  {
    'max_depth': 6,
    'learning_rate': 0.1,
    'subsample': 0.8,
    'colsample_bytree': 0.9
  }
```
- *Tools:* scikit-learn, XGBoost

## 📏 8. Model Evaluation

```bash
Metric | Value
MAE | 9.2
RMSE | 12.8
R² | 0.89
```

- *Observations:*
- Stable performance across junctions (±1.5 MAE)
- Worst case: Friday evening peaks (MAE = 14.3)

  
## 🔍 9. Model Interpretability

- *SHAP Analysis:*
- Top Features: Hour (32%), Junction (28%), DayOfWeek (19%)
- Weekend reduces base prediction by ~15%
- *Tools:* SHAP, matplotlib

- ## 💾 10. Model Saving
- *Format:* .pkl (Python Pickle)

- *Size:* 48 MB

- *Metadata Includes:*

- Feature names

- Data schema

- Model version info

- *Tool:* joblib


## 🚀 11. Deployment
- *Architecture:*

- FastAPI backend with rate limiting

- Docker container hosted on AWS ECS

## 📦 Tech Stack

```bash
pandas, numpy, scikit-learn, XGBoost, matplotlib, seaborn, SHAP, FastAPI, Docker, AWS, Prometheus, Evidently AI
```

## 📫 Let's Connect

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/umeshsamartapu/)
[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://x.com/umeshsamartapu)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:umeshsamartapu@gmail.com)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/umeshsamartapu/)
[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-FBAD19?style=flat-square&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/umeshsamartapu)

---

🔥 Always exploring new technologies and solving real-world problems with code!

