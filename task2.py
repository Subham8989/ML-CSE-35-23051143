# WEB SCRAPING DATA

import requests
from bs4 import BeautifulSoup
import pandas as pd

scrapping_url = "https://books.toscrape.com/"

res = requests.get(scrapping_url)
soup = BeautifulSoup(res.text, "html.parser")

titles = []
prices = []

products = soup.select(".product_pod")

for p in products:
  title = p.h3.a["title"]
  price = p.select_one(".price_color").text.strip()

  titles.append(title)
  prices.append(price)

df = pd.DataFrame({
  "title": titles,
  "price": prices
})

df.to_csv("books_dataset.csv", index=False)
print(df.head())

# API DATA

url = "https://dummyjson.com/products"
res = requests.get(url)
data = res.json()

df = pd.DataFrame(data["products"])
df.to_csv("products.csv", index=False)

print(df.head())