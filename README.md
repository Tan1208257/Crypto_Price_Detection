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

## This project builds a **binary classifier** that predicts whether the next **1-hour** close will be **up (1)** or **down (0)** using only information available up to time *t*.

Requirements covered:
- Uses **rate of change (%)** features rather than absolute values.
- Builds a supervised dataset using a **lookback window** (previous *t* steps).
- Uses the **last year** of data (from the last timestamp) as the **test set** (at minimum).
- Uses **1-hour candles** (resampled from 15m).
- Builds **multiple ML models** and shows **metric improvement** from a baseline model to optimized models.
- Explains **why** each step is done.
- 
## Models Used
- Logistic Regression (baseline)
- Random Forest
- HistGradientBoosting
- XGBoost

## Evaluation Metrics
- Accuracy
- F1-score
- ROC-AUC
- Confusion Matrix

## How to Run
```bat
:: (1) Create & activate a virtual environment
python -m venv .venv
source .venv/Scripts/activate
:: (2) Upgrade pip
python -m pip install --upgrade pip
