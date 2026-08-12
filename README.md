# 📊 Customer Churn AI Agent

An AI-based customer churn prediction and retention recommendation system
developed using the Telco Customer Churn dataset.

## 🎯 Problem Statement

Predict whether a customer is likely to churn and classify the customer
into different risk levels to support customer retention strategies.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Logistic Regression
- Gradio
- Google Colab

## 🤖 Machine Learning Model

Balanced Logistic Regression was used for customer churn prediction.

Class balancing was applied to improve the detection of customers who are
likely to churn.

## 📊 Model Performance

| Metric | Score |
|---|---:|
| Accuracy | 74.75% |
| Precision | 51.59% |
| Recall | 78.07% |
| F1-Score | 62.13% |
| ROC-AUC | 83.47% |

## 🔄 Project Workflow

Dataset
→ Data Preprocessing
→ Exploratory Data Analysis
→ Feature Engineering
→ Logistic Regression
→ Model Evaluation
→ Churn Probability
→ Risk Classification
→ Retention Recommendation
→ Gradio Web Interface

## 🌐 Application

A Gradio-based interactive interface allows users to enter customer
information and receive:

- Churn probability
- Churn risk level
- Retention recommendation

## 📂 Dataset

Telco Customer Churn dataset from Kaggle.

## ▶️ How to Run

Open the `.ipynb` notebook in Google Colab and run the cells sequentially.

The final cell launches the Gradio interface.

## 👩‍💻 Author

Yaswitha Gade
