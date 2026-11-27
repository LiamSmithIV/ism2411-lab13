


import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

# Exercise 1
print("=== Exercise 1: Load ===")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2
print("\n=== Exercise 2: South region ===")
south = df[df['region'] == 'South']
print(len(south))
print(south.head())