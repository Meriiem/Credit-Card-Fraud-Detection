# Credit Card Fraud Detection

This repository contains a machine learning model and a Streamlit web application for detecting credit card fraud. The model is trained on the [Credit Card Fraud Detection dataset from Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), which includes transactions made by credit cards, where we have to identify fraudulent transactions.

## Features

- It uses Logistic Regression, Decision Tree, and Random Forest classifiers for the analysis.
- The Streamlit app allows users to input transaction details and get predictions on whether a transaction is fraud or normal.

## Installation and Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/credit-card-fraud-detection-app.git
   cd credit-card-fraud-detection-app

2. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt

3. **Download the dataset from Kaggle and place it in the root directory of the project:**
  - Download from [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).
  - Ensure the file is named creditcard.csv

4. **Train the model (if not already trained) by running the Jupyter Notebook (model_training.ipynb)**

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py

6. **Visit http://localhost:xxxx in your web browser to interact with the application.**

## Usage

- In the web app, input the transaction details across the provided fields.
- Click the "Predict" button to get the model's prediction on whether the transaction is normal or fraudulent.
