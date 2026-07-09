from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


# ---------------- Browser Setup ----------------

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)


# ---------------- Open Website ----------------

url = "https://coinmarketcap.com/"
driver.get(url)

time.sleep(5)


# Scroll page to load coins
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight/2);"
)

time.sleep(3)


# ---------------- Scraping ----------------

coins = []

rows = driver.find_elements(
    By.XPATH,
    "//table/tbody/tr"
)


for row in rows[:100]:

    try:
        columns = row.find_elements(
            By.TAG_NAME,
            "td"
        )

        name_data = columns[2].text.split("\n")


        if len(name_data) < 2:
            continue


        name = name_data[0]
        symbol = name_data[1]


        # remove unwanted row
        if "CoinMarketCap" in name:
            continue


        price = columns[3].text

        volume = columns[7].text.split("\n")[0]


        # ---------------- Clean Price ----------------

        price = float(
            price.replace("$", "")
            .replace(",", "")
        )


        # ---------------- Clean Volume ----------------

        volume_text = (
            volume.replace("$", "")
            .replace(",", "")
        )


        if "T" in volume_text:

            volume = float(
                volume_text.replace("T", "")
            ) * 1_000_000_000_000


        elif "B" in volume_text:

            volume = float(
                volume_text.replace("B", "")
            ) * 1_000_000_000


        elif "M" in volume_text:

            volume = float(
                volume_text.replace("M", "")
            ) * 1_000_000


        else:

            volume = float(volume_text)



        coins.append(
            {
                "Coin": name,
                "Symbol": symbol,
                "Price": price,
                "Volume_24h": volume
            }
        )


    except Exception:
        continue



# ---------------- Close Browser ----------------

driver.quit()



# ---------------- Save Excel ----------------

df = pd.DataFrame(coins)


# Create price category for slicer

df["Price_Category"] = df["Price"].apply(
    lambda x: "$0-$50" if x <= 50 else "Above $50"
)
# Create Top 5 + Others for each price category

df["Rank"] = (
    df.groupby("Price_Category")["Volume_24h"]
    .rank(method="first", ascending=False)
)


df["Liquidity_Group"] = df.apply(
    lambda row: row["Coin"]
    if row["Rank"] <= 5
    else "Others",
    axis=1
)


df.drop(
    columns=["Rank"],
    inplace=True
)


df.to_excel(
    "crypto_data.xlsx",
    index=False
)


print(df)

print(
    "\nCrypto data saved successfully!"
)