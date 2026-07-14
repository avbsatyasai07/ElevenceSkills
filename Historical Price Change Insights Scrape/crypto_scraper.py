from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# ---------------- Browser Setup ----------------
options = Options()
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

            # 1 Hour %
            change1 = (
                cells[4]
                .text
                .replace("%", "")
                .strip()
            )

            if change1 == "":
                change1 = "0"

            change1 = float(change1)

            # 24 Hour %
            change24 = (
                cells[5]
                .text
                .replace("%", "")
                .strip()
            )

            if change24 == "":
                change24 = "0"

            change24 = float(change24)

            # 7 Day %
            change7 = (
                cells[6]
                .text
                .replace("%", "")
                .strip()
            )

            if change7 == "":
                change7 = "0"

            change7 = float(change7)

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
df = df.drop_duplicates(subset=["Symbol"])

# Reset index
df.reset_index(drop=True, inplace=True)

# Save Excel
df.to_excel(
    "crypto_price_change.xlsx",
    index=False
)

print("\n==============================")
print(df.head(10))
print("==============================")
print("Total Coins:", len(df))
print("Excel File Created Successfully!")