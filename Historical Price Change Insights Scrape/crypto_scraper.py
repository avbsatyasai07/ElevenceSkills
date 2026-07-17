from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# ---------------- Browser Setup ----------------

options = Options()

# Change this path if your Brave Browser is installed elsewhere
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

crypto_data = []


# ---------------- Scrape Function ----------------

def scrape_page(page):

    url = f"https://coinmarketcap.com/?page={page}"

    print(f"\nOpening Page {page}...")

    driver.get(url)
    time.sleep(8)

    rows = driver.find_elements(By.XPATH, "//tbody/tr")

    print(f"Rows Found on Page {page}: {len(rows)}")

    for i in range(len(rows)):

        try:

            rows = driver.find_elements(By.XPATH, "//tbody/tr")
            row = rows[i]

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                row
            )

            time.sleep(0.2)

            cells = row.find_elements(By.TAG_NAME, "td")

            # Skip invalid rows
            if len(cells) != 11:
                continue

            coin_lines = cells[2].text.split("\n")

            if len(coin_lines) < 2:
                continue

            coin_name = coin_lines[0]
            symbol = coin_lines[1]

            # Skip CoinMarketCap Index
            if coin_name == "CoinMarketCap 20 Index DTF":
                continue

            # Current Price
            current_price = (
                cells[3]
                .text
                .replace("$", "")
                .replace(",", "")
                .strip()
            )

            if current_price == "":
                continue

            current_price = float(current_price)

            # 1 Hour Change %
            change1 = (
                cells[4]
                .text
                .replace("%", "")
                .strip()
            )

            if change1 == "":
                change1 = "0"

            change1 = abs(float(change1))

            # 24 Hour Change %
            change24 = (
                cells[5]
                .text
                .replace("%", "")
                .strip()
            )

            if change24 == "":
                change24 = "0"

            change24 = abs(float(change24))

            # 7 Day Change %
            change7 = (
                cells[6]
                .text
                .replace("%", "")
                .strip()
            )

            if change7 == "":
                change7 = "0"

            change7 = abs(float(change7))

            crypto_data.append([
                coin_name,
                symbol,
                round(current_price, 6),
                round(change1, 4),
                round(change24, 4),
                round(change7, 4)
            ])

        except Exception as e:
            print(f"Skipped Row {i}: {e}")


# ---------------- Scrape Both Pages ----------------

scrape_page(1)
scrape_page(2)

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

# Remove duplicate symbols
df.drop_duplicates(
    subset=["Symbol"],
    inplace=True
)

# Reset index
df.reset_index(
    drop=True,
    inplace=True
)


# ---------------- Average Downfall Percentage ----------------

df["Average Downfall %"] = (
    df["1H Change %"] +
    df["24H Change %"] +
    df["7D Change %"]
) / 3

df["Average Downfall %"] = df[
    "Average Downfall %"
].round(4)


# ---------------- Price Range Categorization ----------------

def price_range(price):

    if price <= 0.05:
        return "$0 - $0.05"

    elif price <= 0.5:
        return "$0.05 - $0.5"

    elif price <= 5:
        return "$0.5 - $5"

    elif price <= 50:
        return "$5 - $50"

    else:
        return ">$50"


df["Price Range"] = df["Current Price"].apply(price_range)


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

file_name = "low_budget_investment_insights.xlsx"

df.to_excel(
    file_name,
    index=False
)


# ---------------- Output ----------------

print("\n==============================")
print(df.head(10))
print("==============================")

print("\nTotal Coins Scraped :", len(df))
print("\nExcel File Created Successfully!")
print(f"File Name : {file_name}")