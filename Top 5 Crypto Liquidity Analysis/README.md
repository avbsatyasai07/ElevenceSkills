# Top 5 Crypto Liquidity Analysis Dashboard

## 📌 Project Overview

This project is developed as part of the **Elevence Skills Data Analytics Internship**.

The objective of this project is to analyze cryptocurrency liquidity distribution using **24-hour trading volume** and create an interactive Excel dashboard.

The dashboard allows users to filter cryptocurrencies based on price ranges and visualize the **Top 5 cryptocurrencies with highest liquidity**, while grouping all remaining coins into an **"Others"** category.

---

## 🎯 Problem Statement

Create a pie chart that shows the liquidity distribution of cryptocurrency coins based on their **24-hour trading volume**.

Requirements:

- Create a slicer to divide coins into:
  - `$0 - $50`
  - `Above $50`

- Based on the selected price category:
  - Display the Top 5 coins by Volume (24h)
  - Combine remaining coins into an **Others** category

- The pie chart should dynamically update when the slicer value changes.

---

## ✨ Features

✔ Live cryptocurrency data extraction  
✔ Automatic data cleaning  
✔ Price based categorization  
✔ Top 5 liquidity ranking  
✔ Automatic "Others" grouping  
✔ Dynamic Excel slicer filtering  
✔ Interactive pie chart dashboard  

---

## 🛠 Technologies Used

- Python
- Selenium
- Pandas
- OpenPyXL
- Microsoft Excel
- Pivot Tables
- Excel Slicers
- Pivot Charts

---

## 📂 Project Structure

```
Top 5 Crypto Liquidity Analysis

│
├── crypto_scraper.py
│
├── Top_5_Crypto_Liquidity_Analysis.xlsx
│
├── crypto_data.xlsx
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## 📊 Dataset Information

The cryptocurrency data is collected from CoinMarketCap.

Extracted fields:

| Column | Description |
|---|---|
| Coin | Cryptocurrency name |
| Symbol | Coin short symbol |
| Price | Current market price |
| Volume_24h | 24-hour trading volume |
| Price_Category | Price range classification |
| Liquidity_Group | Top coins and Others grouping |

Example:

| Coin | Price | Volume_24h | Price_Category |
|---|---|---|---|
| Bitcoin | 62742 | 1250000000000 | Above $50 |
| XRP | 1.09 | 68550000000 | $0-$50 |

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <repository-link>
```

Move into project folder:

```bash
cd "Top 5 Crypto Liquidity Analysis"
```

---

## Step 2: Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

---

## Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

Required packages:

- selenium
- pandas
- openpyxl

---

# 🚀 Running the Project

Run:

```bash
python crypto_scraper.py
```

The script will:

1. Open browser automatically
2. Collect cryptocurrency data
3. Clean price and volume values
4. Create price categories
5. Generate Top 5 + Others grouping
6. Export data into Excel


Output file generated:

```
crypto_data.xlsx
```

---

# 📈 Dashboard Creation

The Excel dashboard contains:

## Price Category Slicer

Filters:

```
$0-$50

Above $50
```

---

## Liquidity Distribution Pie Chart

Example output:

```
Bitcoin
Ethereum
BNB
Solana
Hyperliquid
Others
```

The "Others" section represents the combined volume of all remaining coins outside the Top 5.

---

# 🔄 Dashboard Working Process


```
Crypto Data

      ↓

Price Category Filter

      ↓

Select Top 5 Coins By Volume

      ↓

Group Remaining Coins

      ↓

Dynamic Pie Chart
```

---

# 📌 Key Learning Outcomes

Through this project:

- Automated data collection using Selenium
- Data cleaning using Pandas
- Working with financial datasets
- Excel dashboard development
- Pivot Table analysis
- Interactive visualization using slicers

---

# 📷 Dashboard Preview

Add dashboard screenshot here.

---

# 👨‍💻 Author

**Veera Bala Satya Sai Appana**

Data Analytics Internship Project  
Elevence Skills
