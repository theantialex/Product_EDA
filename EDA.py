import pandas as pd

def clean_percentage(val):
    return int(val[:val.index('%')])

def clean_size(val):
    if val == 'Nan':
        val = None
    elif 'Size:' in val:
        val = val[val.index(':') + 1:]
    return val

# Make columns visible
pd.set_option('max_columns', 100)

# Load the dataset
df = pd.read_csv('Product_DataSet.csv')

# Describe the dataset
print(df.info())

# Rename columns
df = df.rename(columns={'BrandName':'Brand_Name',
                   'Product ID':'Product_ID',
                   'Product Name':'Product_Name',
                   'Brand Desc':'Brand_Desc',
                   'Product Size':'Product_Size',
                   'SellPrice':'Sell_Price'})

# Check for NaN values
print(df.isna().sum())

# Check for duplicated values
print(df.loc[df.duplicated()])

# Display the first few rows of the dataset
print(df.head())

# Check out and clean up discount values
print(df['Discount'].value_counts())
print((~df['Discount'].str.contains('% off')).sum())

df['Discount'] = df['Discount'].apply(clean_percentage)

# Check out and clean up product size values
print(df['Product_Size'].value_counts())

df['Product_Size'] = df['Product_Size'].apply(clean_size)

# Summary statistics 
print(df.describe())