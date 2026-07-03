# Time-Based Visibility & Sentiment Analysis

## Project Overview

This project is developed as part of the **Elevance Skills Data Analytics Internship**.

The project combines **Web Scraping, Data Processing, Excel Dashboarding, Sentiment Analysis, and VBA Automation** to build a cryptocurrency monitoring dashboard.

The application scrapes live cryptocurrency market data from **CoinMarketCap**, filters the required coins according to the task specification, performs sentiment analysis based on the 24-hour price movement, exports the processed data into Excel, and displays the **Top 10 cryptocurrencies by 24-hour trading volume**.

The dashboard includes **time-based visibility control** using VBA. The chart is visible only during working hours (9:00 AM – 5:00 PM). Outside these hours, the dashboard displays a message asking the user to open it during working hours.

---

# Objectives

* Scrape live cryptocurrency market data.
* Process and clean the extracted data.
* Perform simple sentiment analysis.
* Filter cryptocurrencies according to task requirements.
* Display Top 10 cryptocurrencies based on 24-hour trading volume.
* Build an Excel dashboard.
* Automate dashboard visibility using VBA.
* Refresh dashboard automatically.

---

# Technologies Used

### Programming Language

* Python 3.x

### Libraries

* Selenium
* Pandas
* OpenPyXL

### Tools

* Microsoft Excel
* VBA (Visual Basic for Applications)
* Brave Browser
* ChromeDriver

---

# Project Structure

```
Time-Based Visibility & Sentiment Analysis
│
├── scrape_crypto.py
├── inspect_table.py
├── requirements.txt
├── crypto_data.xlsx
├── crypto_data.xlsm
└── README.md
```

---

# Data Source

Website Used:

https://coinmarketcap.com/

The project scrapes the following cryptocurrency information:

* Rank
* Coin Name
* Symbol
* Price (USD)
* 1 Hour Change
* 24 Hour Change
* 7 Day Change
* Market Capitalization
* 24 Hour Trading Volume
* Circulating Supply

---

# Workflow

## Step 1 – Web Scraping

The Python script uses Selenium to:

* Launch Brave Browser.
* Open CoinMarketCap.
* Scroll automatically to load cryptocurrency data.
* Extract cryptocurrency information from the market table.
* Store the extracted data inside a Pandas DataFrame.

---

## Step 2 – Data Cleaning

The extracted data is cleaned by:

* Removing commas
* Removing dollar symbols
* Converting percentages into numeric values
* Converting Market Cap and Volume into numeric values for proper sorting

---

## Step 3 – Sentiment Analysis

Sentiment is determined using the 24-hour price change.

Rules:

Positive

* 24h Change > 2%

Negative

* 24h Change < -2%

Neutral

* Between -2% and +2%

---

## Step 4 – Filtering

The task requires displaying only cryptocurrencies whose names begin with:

* A
* E
* I
* O
* U
* B
* C
* D

The program filters only those cryptocurrencies.

---

## Step 5 – Top 10 Selection

After filtering:

* Coins are sorted using **24-hour Trading Volume**.
* Top 10 cryptocurrencies are selected.

---

## Step 6 – Excel Export

The processed data is exported into three worksheets.

### All Coins

Contains every scraped cryptocurrency.

### Filtered Coins

Contains only cryptocurrencies satisfying the filtering condition.

### Top 10

Contains the Top 10 cryptocurrencies sorted by Volume (24h).

---

## Step 7 – Dashboard

A Dashboard worksheet is created in Excel containing:

* Top 10 cryptocurrency table
* Column Chart
* Last Refreshed timestamp
* Working Hours message

---

## Step 8 – VBA Automation

VBA automatically checks the current system time.

If current time is between:

```
09:00 AM
to
05:00 PM
```

The dashboard chart is displayed.

Otherwise:

The chart is hidden and the following message is displayed:

```
Please open in working hours
(9 am to 5 pm)
```

---

# Features

* Live Cryptocurrency Data Scraping
* Selenium Automation
* Brave Browser Support
* Data Cleaning
* Sentiment Analysis
* Top 10 Volume Ranking
* Excel Dashboard
* VBA Automation
* Automatic Dashboard Refresh
* Time-Based Dashboard Visibility

---

# Output

Python generates:

```
crypto_data.xlsx
```

The final dashboard is available in:

```
crypto_data.xlsm
```

---

# How to Run

## 1. Clone Repository

```
git clone <repository_url>
```

---

## 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## 3. Run Python Script

```
python scrape_crypto.py
```

This generates:

```
crypto_data.xlsx
```

---

## 4. Open Dashboard

Open

```
crypto_data.xlsm
```

Enable Macros when prompted.

The dashboard automatically checks the current time and controls chart visibility.

---

# Expected Output

* Live cryptocurrency data
* Filtered cryptocurrency list
* Top 10 by Volume
* Sentiment Analysis
* Excel Dashboard
* Automatic VBA-controlled chart visibility

---

# Learning Outcomes

This project demonstrates practical knowledge of:

* Web Scraping
* Selenium Automation
* Data Cleaning
* Data Analysis
* Excel Automation
* VBA Programming
* Dashboard Development
* Financial Data Processing
* Automation using Python and Excel

---

# Author

**Veera Bala Satya Sai Appana**

B.Tech – Data Science

Aditya University

Elevance Skills Data Analytics Internship
