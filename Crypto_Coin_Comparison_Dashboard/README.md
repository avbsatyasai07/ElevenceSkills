# Crypto Coin Comparison Dashboard

## Project Overview

This project was developed as part of the Elevence Skills Data Analytics Internship.

The Crypto Coin Comparison Dashboard is an Excel-based analytics dashboard that allows users to compare two cryptocurrencies by entering their coin names.

The project uses Python web scraping to collect cryptocurrency data and Microsoft Excel features such as XLOOKUP, Data Validation, and KPI calculations to perform comparison analysis.

---

## Objective

Create a dashboard where users can input two crypto coin names and compare:

- Symbol
- Price
- Volume
- Market Capitalization
- Circulating Supply

The dashboard also calculates KPI indicators showing the differences between selected cryptocurrencies.

---

## Technologies Used

### Programming

- Python

### Python Libraries

- Selenium
- Pandas
- OpenPyXL

### Dashboard Tool

- Microsoft Excel

### Development Tool

- VS Code

---

## Data Collection

Cryptocurrency data is collected from CoinMarketCap using Selenium web scraping.

The scraper extracts:

- Coin Name
- Symbol
- Price
- Volume
- Market Capitalization
- Circulating Supply

The extracted data is stored automatically in an Excel file.

---

## Workflow

```
CoinMarketCap Website
          |
          ↓
Python Selenium Scraper
          |
          ↓
Data Processing with Pandas
          |
          ↓
Excel Dataset Creation
          |
          ↓
Crypto Comparison Dashboard
```

---

# Dashboard Features

## Crypto Comparison Table

Users enter two cryptocurrency names.

Example:

```
Coin 1: Bitcoin

Coin 2: Ethereum
```

The dashboard automatically displays:

| Details | Coin 1 | Coin 2 |
|---|---|---|
| Symbol | Auto Filled | Auto Filled |
| Price | Auto Filled | Auto Filled |
| Volume | Auto Filled | Auto Filled |
| Market Capitalization | Auto Filled | Auto Filled |
| Circulating Supply | Auto Filled | Auto Filled |

The values are retrieved using Excel XLOOKUP functions.

---

# KPI Indicators

The dashboard contains three KPI indicators:

## 1. Volume Difference

Calculates the difference between the trading volumes of the selected coins.

## 2. Market Capitalization Difference

Calculates the difference between market capitalization values.

## 3. Circulating Supply Difference

Calculates the difference between available circulating supplies.

---

# Data Validation

Input validation rules are applied to coin name fields.

Rules:

- Coin name must contain minimum 3 characters
- Coin name must contain maximum 10 characters
- Numbers are not allowed

Valid inputs:

```
Bitcoin
Ethereum
Solana
```

Invalid inputs:

```
BT

Bitcoin123

VeryLongCoinName
```

---

# How To Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the scraper:

```bash
python crypto_scraper.py
```

After successful execution:

```
Crypto data scraped successfully
```

The Excel dataset will be generated.

---

# Project Structure

```
Crypto_Coin_Comparison_Dashboard

│
├── crypto_scraper.py
├── crypto_data.xlsx
├── Crypto_Coin_Comparison_Dashboard.xlsx
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Key Learning Outcomes

- Web Scraping using Selenium
- Data Processing using Pandas
- Excel Dashboard Creation
- XLOOKUP Implementation
- KPI Analysis
- Excel Data Validation

---

# Conclusion

This project demonstrates how Python data extraction can be combined with Excel analytics to create an interactive cryptocurrency comparison dashboard.