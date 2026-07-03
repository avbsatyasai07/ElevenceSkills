from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

# ==========================
# Helper Functions
# ==========================

def convert_money(value):
    value = value.replace("$", "").replace(",", "").strip()

    multiplier = 1

    if value.endswith("T"):
        multiplier = 1_000_000_000_000
        value = value[:-1]

    elif value.endswith("B"):
        multiplier = 1_000_000_000
        value = value[:-1]

    elif value.endswith("M"):
        multiplier = 1_000_000
        value = value[:-1]

    elif value.endswith("K"):
        multiplier = 1_000
        value = value[:-1]

    try:
        return float(value) * multiplier
    except:
        return 0


def convert_percent(value):
    try:
        return float(value.replace("%", "").replace(",", "").strip())
    except:
        return 0


# ==========================
# Brave Browser
# ==========================

options = Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

driver = webdriver.Chrome(options=options)

print("Opening CoinMarketCap...")

driver.get("https://coinmarketcap.com/")

time.sleep(8)

# ==========================
# Scroll Page
# ==========================

last_height = 0

while True:

    driver.execute_script("window.scrollBy(0,1000);")

    time.sleep(1)

    new_height = driver.execute_script("return window.pageYOffset")

    if new_height == last_height:
        break

    last_height = new_height

rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

print(f"Rows Found : {len(rows)}")

# ==========================
# Extract Data
# ==========================

crypto_data = []

for row in rows:

    try:

        cells = row.find_elements(By.TAG_NAME, "td")

        if len(cells) < 10:
            continue

        rank = cells[1].text.strip()

        if not rank.isdigit():
            continue

        coin = cells[2].find_element(
            By.CLASS_NAME,
            "coin-item-name"
        ).text.strip()

        symbol = cells[2].find_element(
            By.CLASS_NAME,
            "coin-item-symbol"
        ).text.strip()

        price = convert_money(cells[3].text)

        change_1h = convert_percent(cells[4].text)

        change_24h = convert_percent(cells[5].text)

        change_7d = convert_percent(cells[6].text)

        market_cap = convert_money(cells[7].text)

        volume = convert_money(cells[8].text)

        circulating_supply = cells[9].text.strip()

        # Sentiment

        if change_24h > 2:
            sentiment = "Positive"

        elif change_24h < -2:
            sentiment = "Negative"

        else:
            sentiment = "Neutral"

        crypto_data.append({

            "Rank": int(rank),

            "Coin Name": coin,

            "Symbol": symbol,

            "Price (USD)": price,

            "1h Change (%)": change_1h,

            "24h Change (%)": change_24h,

            "7d Change (%)": change_7d,

            "Market Cap": market_cap,

            "Volume (24h)": volume,

            "Circulating Supply": circulating_supply,

            "Sentiment": sentiment

        })

    except Exception:
        continue

driver.quit()

# ==========================
# Create DataFrame
# ==========================

df = pd.DataFrame(crypto_data)

print("\nTotal Coins Scraped:", len(df))

print(df.head())

# ==========================
# Filter Task Requirement
# ==========================

letters = ("A", "E", "I", "O", "U", "B", "C", "D")

filtered = df[
    df["Coin Name"].str.startswith(letters)
]

# ==========================
# Top 10 by Volume
# ==========================

top10 = filtered.sort_values(
    by="Volume (24h)",
    ascending=False
).head(10)

# ==========================
# Save Excel
# ==========================

with pd.ExcelWriter("crypto_data.xlsx", engine="openpyxl") as writer:

    df.to_excel(
        writer,
        sheet_name="All Coins",
        index=False
    )

    filtered.to_excel(
        writer,
        sheet_name="Filtered Coins",
        index=False
    )

    top10.to_excel(
        writer,
        sheet_name="Top 10",
        index=False
    )

print("\nExcel file created successfully!")

print("\nTop 10 Coins\n")

print(
    top10[
        [
            "Coin Name",
            "Volume (24h)",
            "Sentiment"
        ]
    ]
)