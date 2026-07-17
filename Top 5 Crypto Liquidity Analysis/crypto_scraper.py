from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


# ---------------- Browser Setup ----------------

options = Options()

# Chrome for Testing Path
options.binary_location = (
    r"D:\ChromeForTesting\chrome-win64\chrome.exe"
)

options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# Store scraped data
crypto_data = []


# ---------------- Scrape Function ----------------

def scrape_page(page):

    url = f"https://coinmarketcap.com/?page={page}"

    print(f"\nOpening Page {page}...")

    driver.get(url)
    time.sleep(8)

    rows = driver.find_elements(By.XPATH, "//tbody/tr")

    print(f"Rows Found on Page {page}: {len(rows)}")

    for row in rows:

        try:

            cells = row.find_elements(By.TAG_NAME, "td")

            # Skip unwanted rows
            if len(cells) != 11:
                continue

            coin_lines = cells[2].text.split("\n")

            if len(coin_lines) < 2:
                continue

            coin_name = coin_lines[0]
            symbol = coin_lines[1]

            # Skip CoinMarketCap Index row
            if "CoinMarketCap" in coin_name:
                continue

            # ---------------- Current Price ----------------

            price = (
                cells[3]
                .text
                .replace("$", "")
                .replace(",", "")
                .strip()
            )

            if price == "":
                continue

            price = float(price)

            # ---------------- 1 Hour Change % ----------------

            change_1h = (
                cells[4]
                .text
                .replace("%", "")
                .strip()
            )

            if change_1h == "":
                change_1h = "0"

            change_1h = abs(float(change_1h))

            # ---------------- 24 Hour Change % ----------------

            change_24h = (
                cells[5]
                .text
                .replace("%", "")
                .strip()
            )

            if change_24h == "":
                change_24h = "0"

            change_24h = abs(float(change_24h))

            # ---------------- 7 Day Change % ----------------

            change_7d = (
                cells[6]
                .text
                .replace("%", "")
                .strip()
            )

            if change_7d == "":
                change_7d = "0"

            change_7d = abs(float(change_7d))

            # Store the data
            crypto_data.append(
                [
                    coin_name,
                    symbol,
                    round(price, 6),
                    round(change_1h, 4),
                    round(change_24h, 4),
                    round(change_7d, 4)
                ]
            )

        except Exception:
            continue


# ---------------- Scrape Both Pages ----------------

scrape_page(1)
scrape_page(2)

# Close browser
driver.quit()


# ---------------- Create DataFrame ----------------

df = pd.DataFrame(
    crypto_data,
    columns=[
        "Coin Name",
        "Symbol",
        "Current Price",
        "1H Change %",
        "24H Change %",
        "7D Change %"
    ]
)


# ---------------- Remove Duplicate Coins ----------------

df.drop_duplicates(
    subset=["Symbol"],
    inplace=True
)

df.reset_index(
    drop=True,
    inplace=True
)


# ---------------- Keep Only 200 Coins ----------------

df = df.head(200)

df.reset_index(
    drop=True,
    inplace=True
)


# ---------------- Average Downfall Percentage ----------------

df["Average Downfall %"] = (

    df["1H Change %"]
    + df["24H Change %"]
    + df["7D Change %"]

) / 3

df["Average Downfall %"] = (
    df["Average Downfall %"]
    .round(4)
)


# ---------------- Price Range Categorization ----------------

def price_range(price):

    if price <= 0.05:
        return "$0-$0.05"

    elif price <= 0.5:
        return "$0.05-$0.5"

    elif price <= 5:
        return "$0.5-$5"

    elif price <= 50:
        return "$5-$50"

    else:
        return ">$50"


df["Price Range"] = (
    df["Current Price"]
    .apply(price_range)
)


# ---------------- Sort by Least Average Downfall ----------------

df.sort_values(
    by="Average Downfall %",
    inplace=True
)

df.reset_index(
    drop=True,
    inplace=True
)


# ---------------- Save Excel File ----------------

df.to_excel(
    "low_budget_investment_insights.xlsx",
    index=False
)


# ---------------- Output ----------------

print("\n==============================")
print(df.head(10))
print("==============================")

print("\nTotal Coins :", len(df))

print("\nExcel File Created Successfully!")