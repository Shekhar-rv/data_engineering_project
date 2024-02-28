from pandas import read_csv # type: ignore


data = read_csv("/de_project/src/data/car_prices.csv")

# print(data.info())

print(data.columns)

print(f"Unique makes before: {data['make'].nunique()}")

data['make'] = data['make'].str.title() # type: ignore

print(f"Unique makes after: {data['make'].nunique()}")

print(data['make'].unique()) # type: ignore
