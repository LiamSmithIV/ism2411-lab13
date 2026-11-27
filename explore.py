


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

# Exercise 3
print("\n=== Exercise 3: Top 5 by revenue ===")
top5 = df.sort_values('revenue', ascending=False).head(5)
print(top5)

# Exercise 4
print("\n=== Exercise 4: South and revenue over 1000 ===")
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head())

# Exercise 5
print("\n=== Exercise 5: Revenue per unit ===")
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

# Exercise 6
print("\n=== Exercise 6: Regions ===")
print(df['region'].unique())
print(df['region'].value_counts())

# Exercise 7
print("\n=== Exercise 7: Select columns ===")
subset = df[['region', 'product', 'revenue']]
print(subset.shape)

# Exercise 8
print("\n=== Exercise 8: Save ===")
df.to_csv('data/explored.csv', index=False)
print("Saved data/explored.csv")