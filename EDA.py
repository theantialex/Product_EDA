import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

def clean_percentage(val):
    return int(val[:val.index('%')])

def clean_size(val):
    if val == 'Nan':
        val = None
    elif 'Size:' in val:
        val = val[val.index(':') + 1:]
    return val

def clean_MRP(row):
    if isinstance(row['MRP'], float) or isinstance(row['MRP'], int) or (isinstance(row['MRP'], str) and row['MRP'].isdigit()):
        return float(row['MRP'])
    return row['Sell_Price']

# Make columns visible
pd.set_option('max_columns', 100)

# Update plot style
plt.style.use('ggplot')

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

# Check out and clean up MRP values
print(df['MRP'].unique())

df['MRP'] = df.apply(clean_MRP, axis=1)

# Add new columns
df['Actual_Price'] = df.Sell_Price * (1-df.Discount/100)
df['Diff_MRP_Price'] = df.MRP - df.Sell_Price

# Check out and clean up product size values
print(df['Product_Size'].value_counts())

df['Product_Size'] = df['Product_Size'].apply(clean_size)

# Summary statistics 
print(df.describe())

# Bar chart for top 10 brands by products amount
ax = df['Brand_Name'].value_counts() \
    .head(10) \
    .plot(kind='barh', title='Top 10 Brands by Products Amount')

ax.set_xlabel('Product Count')
ax.set_ylabel('Brand Name')
ax.invert_yaxis()

plt.savefig('top_brands.png')
plt.show()


# Pie chart for category distribution
bx = df['Category'].value_counts() \
    .plot(kind='pie', title='Categories Distribution', autopct='%1.1f%%',).axis('off')

plt.savefig('categories.png')
plt.show()

# Overall pricing strategies

# Sell_Price vs Discount with Categories
plt.figure(figsize=(8,4))
cx = sns.scatterplot(x='Discount',
                y='Sell_Price',
                hue='Category',
                data=df)
cx.set_title('Prices and Discounts')
cx.set_ylabel('Price')

plt.savefig('prices_discounts.png')
plt.show()

# Group by Category and sum the MRT and Sell_Price values
grouped_df = df.groupby('Category').sum()
grouped_df = grouped_df[[ 'MRP', 'Sell_Price', 'Actual_Price']]

grouped_df.plot(kind='bar')

plt.title('MRP and Price by Category')
plt.xlabel('Category')
plt.ylabel('Sum')
plt.legend(title='Metric', loc='upper left')

plt.xticks(rotation=40)
plt.tight_layout()

plt.savefig('MRP_prices.png')
plt.show()

# Identify and loc top 10 brands
brands = df['Brand_Name'].value_counts().head(10).keys()
new_df = df.loc[df['Brand_Name'].isin(brands)]

# Stacked Bar Chart of Category by Brand (top 10 stats)
# Group the data by brand and category, and count the occurrences
grouped_data = new_df.groupby(['Brand_Name', 'Category']).size().unstack()
grouped_data.plot(kind='bar', stacked=True)

plt.title('Category Count by Brand')
plt.xlabel('Brand')
plt.ylabel('Category')
plt.legend(title='Categories by Brand', loc='upper left')

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig('categories_by_brands.png')
plt.show()

# Brand specific pricing patterns (top 10 stats)
dx = sns.scatterplot(x='Brand_Name',
                y='Actual_Price',
                hue='Category',
                data=new_df)
dx.set_title('Prices and Brands')
dx.set_xlabel('Brand')
dx.set_ylabel('Price')
plt.legend(title='Metric', loc='upper left')

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig('brand_pricing.png')
plt.show()
