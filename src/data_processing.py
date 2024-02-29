from pandas import read_csv # type: ignore


data = read_csv("/de_project/src/data/car_prices.csv")

# print(data.info())

print(data.columns)

print(f"Unique makes before: {data['make'].nunique()}")

print("length of data before removing duplicates: ", len(data))

data['make'] = data['make'].str.title() # type: ignore

print(f"Unique makes after: {data['make'].nunique()}")

# remove all rows with nan values
data = data.dropna()

print(data['make'].unique()) # type: ignore

for row in data['make']:
    item = row.split(' ')
    if len(item) > 1 and item[1] == 'Tk':
        # replace the value with the first part of the string
        data['make'].replace(row, item[0], inplace=True)

print(data['make'].unique()) # type: ignore

print(f"Unique makes after removing tk: {data['make'].nunique()}")

print("length of data after removing duplicates: ", len(data))