import numpy as np
import pandas as pd

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

dataset = np.zeros((rows, cols), dtype=int)

for i in range(rows):
  for j in range(cols):
    dataset[i, j] = np.random.randint(1, 101)

df = pd.DataFrame(dataset, columns=[chr(i + 65) for i in range(cols)])

print(df)

df.to_csv("data.csv")