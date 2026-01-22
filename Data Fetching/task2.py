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

# COLLECTING DATA FROM CSV

import csv

with open("data/employee_salary_10.csv", "r") as fp:
  file = csv.reader(fp)
  counter = 0
  for lines in file:
    if counter == 5:
      break
    print(lines)
    counter += 1

import json

with open("data/sample.json", "r") as fp:
  aqi_data = json.load(fp)

if isinstance(aqi_data, list) and len(aqi_data) > 0:
  headers = aqi_data[0].keys()

  with open("output.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(aqi_data)

    print("AQI.json converted to AQI.csv successfully.")

else:
    print("JSON format not supported (expected a list of dictionaries).")
