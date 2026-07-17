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


# ---------------- Helper Function ----------------

def clean_percentage(value):

    value = (
        value.replace("%", "")
        .replace("<", "")
        .replace(">", "")
        .strip()
    )

    if value in ["", "--"]:
        return 0.0

    try:
        return abs(float(value))
    except:
        return 0.0


# ---------------- Scrape Function ----------------

def scrape_page(page):

    url = f"https://coinmarketcap.com/?page={page}"

    print(f"\nOpening Page {page}...")

    driver.get(url)
    time.sleep(5)

    # Scroll slowly to load all coins
    for _ in range(25):

        driver.execute_script(
            "window.scrollBy(0, 800);"
        )

        time.sleep(0.7)

    time.sleep(3)

    rows = driver.find_elements(
        By.XPATH,
        "//tbody/tr"
    )

    print(
        f"Rows Found on Page {page}: {len(rows)}"
    )

    for row in rows:

        coin_name = "Unknown"

        try:

            cells = row.find_elements(
                By.TAG_NAME,
                "td"
            )

            # We only need up to column index 6
            if len(cells) < 7:
                continue

            coin_lines = (
                cells[2]
                .text
                .split("\n")
            )

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

            if price in ["", "--"]:
                continue

            try:
                price = float(price)
            except:
                continue


            # ---------------- Percentage Changes ----------------

            change_1h = clean_percentage(
                cells[4].text
            )

            change_24h = clean_percentage(
                cells[5].text
            )

            change_7d = clean_percentage(
                cells[6].text
            )


            # ---------------- Store Data ----------------

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

        except Exception as e:

            print(
                f"Skipped {coin_name} : {e}"
            )

            continue


# ---------------- Scrape Both Pages ----------------

scrape_page(1)
scrape_page(2)

# Close Browser
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

file_name = (
    "low_budget_investment_insights.xlsx"
)

df.to_excel(

    file_name,
    index=False

)


# ---------------- Output ----------------

print("\n==============================")
print(df.head(10))
print("==============================")

print("\nTotal Coins :", len(df))

print("\nExcel File Created Successfully!")
print(f"\nFile Name : {file_name}")