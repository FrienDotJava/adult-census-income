# Income Classification Project

*TRY STREAMLIT APP HERE: https://friendotjava-adult-census-income-dashboard-skdgmi.streamlit.app/*

This project classifies whether an individual's income exceeds $50K/year based on the Adult Census Income dataset. The classification task involves multiple machine learning models, hyperparameter tuning, and evaluation metrics to ensure robust performance.

## Dataset

The [Adult Census Income Dataset](https://archive.ics.uci.edu/ml/datasets/adult) contains demographic and employment-related attributes for individuals. The target variable is `income`, indicating whether an individual's income is `<=50K` or `>50K`.

### Features:
- **Categorical Attributes:**
  - Workclass
  - Education
  - Marital Status
  - Occupation
  - Relationship
  - Race
  - Sex
  - Native Country
- **Numerical Attributes:**
  - Age
  - Final Weight (fnlwgt)
  - Education Number
  - Capital Gain
  - Capital Loss
  - Hours per Week

### Target:
- Binary classification: `<=50K` or `>50K`

## Models Used

The following machine learning models were implemented and evaluated:
1. **Logistic Regression**
2. **K-Nearest Neighbors (KNN)**
3. **Decision Tree**
4. **Support Vector**
5. **Random Forest**
6. **AdaBoost**
7. **Gradient Boosting**

## Steps and Methodology

1. **Data Preprocessing:**
   - Handling missing values
   - Encoding categorical features using one-hot encoding
   - Standardization of numerical features
   - Splitting data into training and testing sets

2. **Exploratory Data Analysis (EDA):**
   - Analyzing feature distributions
   - Identifying correlations
   - Visualizing categorical distributions

3. **Model Implementation:**
   - Training each model with default parameters
   - Pick the best-performing model and improve it using hyperparameter tuning
   - Hyperparameter tuning using RandomizedSearchCV

4. **Evaluation:**
   - Metrics: Accuracy, Precision, Recall, F1-score, ROC-AUC
   - Comparison of model performance

## Hyperparameter Tuning

Hyperparameter tuning was applied to optimize model performance. 

## Results (Default Parameter)

| Model              | Accuracy | Precision | Recall | F1-Score |
|--------------------|----------|-----------|--------|----------|
| Logistic Regression| 84.81%   | 72.74%    | 60.87% | 66.27%   |
| KNN                | 82.78%   | 65.99%    | 61.37% | 63.59%   |
| Decision Tree      | 80.92%   | 60.91%    | 61.83% | 61.37%   |
| Support Vector     | 85.36%   | 75.17%    | 60.17% | 66.84%   |
| Random Forest      | 84.92%   | 71.70%    | 63.57% | 67.39%   |
| AdaBoost           | 81.78%   | 62.53%    | 64.08% | 63.29%   |
| Gradient Boosting  | 86.23%   | 76.94%    | 62.57% | 69.01%   |

## Results (After Parameter Tuning)
| Model              | Accuracy | Precision | Recall | F1-Score |
|--------------------|----------|-----------|--------|----------|
| Gradient Boosting  | 87.18%   | 78.10%    | 66.32% | 71.73%   |
