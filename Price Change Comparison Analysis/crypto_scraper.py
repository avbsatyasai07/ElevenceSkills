from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# ---------------- Browser Setup ----------------
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://coinmarketcap.com/")
time.sleep(8)

# ---------------- Load all rows ----------------
while True:
    old = len(driver.find_elements(By.XPATH, "//tbody/tr"))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new = len(driver.find_elements(By.XPATH, "//tbody/tr"))

    if old == new:
        break

rows = driver.find_elements(By.XPATH, "//tbody/tr")

print("Rows Found:", len(rows))

crypto_data = []

# ---------------- Extract Data ----------------
for i in range(1, min(len(rows), 101)):

    # Refresh DOM
    rows = driver.find_elements(By.XPATH, "//tbody/tr")
    row = rows[i]

    # Scroll current row into view
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        row
    )

    time.sleep(0.35)

    cells = row.find_elements(By.TAG_NAME, "td")

    if len(cells) != 11:
        continue

    try:

        coin_lines = cells[2].text.split("\n")

        if len(coin_lines) < 2:
            continue

        coin_name = coin_lines[0]
        symbol = coin_lines[1]

        # Skip Index row
        if coin_name == "CoinMarketCap 20 Index DTF":
            continue

        current_price = (
            cells[3]
            .text
            .replace("$", "")
            .replace(",", "")
        )

        if current_price == "":
            continue

        current_price = float(current_price)

        change_1h = (
            cells[4]
            .text
            .replace("%", "")
            .strip()
        )

        if change_1h == "":
            change_1h = 0

        change_1h = float(change_1h)

        previous_price = current_price / (
            1 + change_1h / 100
        )

        price_change = current_price - previous_price

        if current_price < 10:
            price_range = "Up to $10"
        else:
            price_range = ">= $10"

        crypto_data.append([
            coin_name,
            symbol,
            round(current_price,6),
            round(previous_price,6),
            round(change_1h,4),
            round(price_change,6),
            price_range
        ])

    except Exception as e:
        print(f"Skipped Row {i}: {e}")

driver.quit()

# ---------------- DataFrame ----------------

df = pd.DataFrame(
    crypto_data,
    columns=[
        "Coin Name",
        "Symbol",
        "Current Price",
        "Previous 1H Price",
        "1H Change %",
        "Price Change",
        "Price Range"
    ]
)

# Remove duplicates
df = df.drop_duplicates(subset=["Symbol"])

# Sort by Price Change
df = df.sort_values(
    by="Price Change",
    ascending=False
)

# Save ALL rows
df.to_excel(
    "crypto_price_change.xlsx",
    index=False
)

print("\n==============================")
print(df.head(10))
print("==============================")
print("Total Coins:", len(df))
print("Excel File Created Successfully!")