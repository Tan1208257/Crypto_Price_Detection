# Crypto Price Direction Prediction (Machine Learning)

## Project Overview
This project builds a machine learning pipeline to predict the short-term price direction (UP/DOWN) of cryptocurrencies using historical market data from the Bybit exchange.

The task is formulated as a binary classification problem on time-series data.

## Dataset
- Source: Bybit historical crypto data (2020–2026)
- Assets: BTC, ETH, SOL, XRP, ADA
- Timeframe: 15-minute candles

Each asset dataset contains:
- Open, High, Low, Close prices
- Trading volume
- Timestamp

## Objective
Predict whether the closing price at time `t+1` will be higher or lower than at time `t`.

## Methodology
1. Merge multiple crypto datasets into a single universal dataset
2. Perform exploratory data analysis (EDA)
3. Engineer time-series features using past information only
4. Split data chronologically into train, validation, and test sets
5. Train and compare multiple models
6. Select the final model based on robust evaluation metrics

## Models Used
- Logistic Regression (baseline)
- Random Forest
- XGBoost

## Evaluation Metrics
- Accuracy
- F1-score
- ROC-AUC
- Confusion Matrix

## How to Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
