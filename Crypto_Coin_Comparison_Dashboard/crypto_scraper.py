from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


# Connect to already opened Brave
options = webdriver.ChromeOptions()

options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)


driver.get(
    "https://coinmarketcap.com/"
)


time.sleep(8)


coins = []


rows = driver.find_elements(
    By.XPATH,
    "//tbody/tr"
)


for row in rows[:50]:

    try:

        cols = row.find_elements(
            By.TAG_NAME,
            "td"
        )

        info = cols[2].text.split("\n")


        coins.append(
            {
                "Coin Name": info[0],
                "Symbol": info[1],
                "Price": cols[3].text,
                "Volume": cols[8].text,
                "Market Capitalization": cols[7].text,
                "Circulating Supply": cols[9].text
            }
        )

    except:
        continue


df = pd.DataFrame(coins)


df.to_excel(
    "crypto_data.xlsx",
    sheet_name="Crypto_Data",
    index=False
)


print("Crypto data scraped successfully")

print(df)


driver.quit()