import pandas as pd

data = pd.read_csv("/de_project/src/data/car_prices.csv")

# print(data.info())

print(data.columns)

print(f"Unique makes before: {data['make'].nunique()}")

data['make'] = data['make'].str.title()

print(f"Unique makes after: {data['make'].nunique()}")

print(data['make'].unique())