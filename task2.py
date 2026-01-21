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

with open("electric_vehicle_data.csv", "r") as fp: # file pointer
  file = csv.reader(fp)
  counter = 0
  for lines in file:
    if counter == 5:
      break
    print(lines)
    counter += 1

# COLLECTING DATA FROM JSON 

import json

with open("AQI.json", "r") as fp: # file pointer
  aqi_data = json.load(fp)


print(aqi_data)
# counter = 0

# for line in aqi_data: 
#   if counter == 5:
#     break
  
#   print(line)

#   counter += 1