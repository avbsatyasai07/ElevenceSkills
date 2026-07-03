# Time-Based Visibility & Sentiment Analysis

## Cryptocurrency Dashboard using Python, Selenium, Excel and VBA

## Project Overview

This project is developed as part of the **Elevance Skills Data Analytics Internship**.

The project combines **Web Scraping, Data Processing, Excel Dashboarding, Sentiment Analysis, and VBA Automation** to build a cryptocurrency monitoring dashboard.

The application scrapes live cryptocurrency market data from **CoinMarketCap**, processes the extracted data, filters cryptocurrencies according to the task requirements, performs sentiment analysis based on 24-hour price movement, and displays the **Top 10 cryptocurrencies based on 24-hour trading volume**.

The Excel dashboard includes **time-based visibility control using VBA**.  
The dashboard chart is visible only during working hours:

**09:00 AM – 05:00 PM**

Outside working hours, the chart is hidden and a message is displayed asking the user to open the dashboard during working hours.

---

# Objectives

- Scrape live cryptocurrency market data
- Clean and process extracted data
- Perform sentiment analysis
- Filter cryptocurrencies according to requirements
- Display Top 10 cryptocurrencies based on 24-hour volume
- Create an Excel dashboard
- Implement VBA automation
- Control dashboard visibility based on time

---

# Technologies Used

## Programming Language

- Python 3.x

## Python Libraries

- Selenium
- Pandas
- OpenPyXL

## Tools

- Microsoft Excel
- VBA (Visual Basic for Applications)
- Brave Browser
- ChromeDriver

---

# Project Structure

```text
Time-Based Visibility & Sentiment Analysis

│
├── scrape_crypto.py
├── requirements.txt
├── crypto_data.xlsx
├── crypto_data.xlsm
├── screenshots/
│
└── README.md
```

---

# Data Source

Website:

https://coinmarketcap.com/

The project extracts:

- Rank
- Coin Name
- Symbol
- Price (USD)
- 1 Hour Change
- 24 Hour Change
- 7 Day Change
- Market Capitalization
- 24 Hour Trading Volume
- Circulating Supply

---

# Workflow

## Step 1 - Web Scraping

The Python script uses Selenium to:

- Launch Brave Browser
- Open CoinMarketCap website
- Automatically scroll the webpage
- Load cryptocurrency market data
- Extract cryptocurrency information
- Store data in a Pandas DataFrame

---

## Step 2 - Data Cleaning

The extracted data is cleaned by:

- Removing unnecessary symbols
- Removing commas
- Removing dollar symbols
- Converting percentage values into numbers
- Converting Market Cap and Volume values for analysis

---

## Step 3 - Sentiment Analysis

Sentiment analysis is performed using the **24-hour price change percentage**.

Rules:

### Positive

```
24h Change > 2%
```

### Negative

```
24h Change < -2%
```

### Neutral

```
-2% to +2%
```

---

# Step 4 - Cryptocurrency Filtering

According to the task requirements, only cryptocurrencies starting with the following letters are selected:

- A
- E
- I
- O
- U
- B
- C
- D

---

# Step 5 - Top 10 Selection

After filtering:

- Cryptocurrencies are sorted using **Volume (24h)**
- The highest volume cryptocurrencies are selected
- Top 10 results are displayed

---

# Step 6 - Excel Export

The processed data is exported into Excel.

The workbook contains:

## All Coins

Contains all scraped cryptocurrency data.

## Filtered Coins

Contains cryptocurrencies matching the filtering conditions.

## Top 10

Contains the Top 10 cryptocurrencies sorted by 24-hour volume.

---

# Step 7 - Excel Dashboard

The dashboard contains:

- Top 10 cryptocurrency table
- Volume comparison chart
- Sentiment information
- Last refreshed timestamp
- Working hours status message

---

# Step 8 - VBA Time-Based Automation

VBA checks the current system time.

If the current time is:

```
09:00 AM - 05:00 PM
```

The chart is displayed.

Outside this time:

- Chart is hidden
- Warning message is shown

Message:

```
Please open in working hours
(9 AM to 5 PM)
```

---

# Features

- Live Cryptocurrency Data Extraction
- Selenium Web Automation
- Data Cleaning and Processing
- Sentiment Classification
- Cryptocurrency Filtering
- Top 10 Volume Ranking
- Excel Dashboard Creation
- VBA Automation
- Time-Based Chart Visibility Control

---

# Screenshots

Project screenshots are available in:

```
screenshots/
```

Includes:

- Dashboard output
- Chart visibility result
- Working hour validation

---

# How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/avbsatyasai07/ElevenceSkills.git
```

Move into project folder:

```bash
cd "ElevenceSkills/Time-Based Visibility & Sentiment Analysis"
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Browser Setup

This project uses **Brave Browser with Selenium**.

Make sure:

- Brave Browser is installed
- ChromeDriver is installed
- ChromeDriver version matches your browser version
- Browser path is configured correctly in `scrape_crypto.py`

---

## 4. Run Python Script

```bash
python scrape_crypto.py
```

After execution, it generates:

```
crypto_data.xlsx
```

---

# Open Excel Dashboard

Open:

```
crypto_data.xlsm
```

Enable macros when Excel asks.

The VBA automation will automatically check the current time and control chart visibility.

---

# Macro Permission Note

Since VBA macros are used, Excel may disable macros by default.

Enable macros:

```
File
 → Options
 → Trust Center
 → Macro Settings
 → Enable VBA Macros
```

---

# Expected Output

The final output includes:

- Live cryptocurrency dataset
- Filtered cryptocurrency records
- Sentiment analysis results
- Top 10 cryptocurrencies by volume
- Excel dashboard
- VBA-controlled chart visibility

---

# Learning Outcomes

This project demonstrates knowledge of:

- Web Scraping
- Selenium Automation
- Data Cleaning
- Data Analysis
- Financial Data Processing
- Excel Dashboard Development
- VBA Programming
- Python and Excel Integration
- Automation Techniques

---

# Author

**Veera Bala Satya Sai Appana**

B.Tech - Data Science  
Aditya University  

Elevance Skills Data Analytics Internship