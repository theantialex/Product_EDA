# Exploratory Data Analysis - Product DataSet
### Data preporation
After Product Dataset is loaded, initial data exploration is conducted. We get information about given columns and their data types:

```
RangeIndex: 4566 entries, 0 to 4565
Data columns (total 11 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   S.No          4566 non-null   int64 
 1   BrandName     4566 non-null   object
 2   Product ID    4566 non-null   object
 3   Product Name  4566 non-null   object
 4   Brand Desc    4566 non-null   object
 5   Product Size  4566 non-null   object
 6   Currancy      4566 non-null   object
 7   MRP           4553 non-null   object
 8   SellPrice     4566 non-null   int64 
 9   Discount      4566 non-null   object
 10  Category      4566 non-null   object
dtypes: int64(2), object(9)
memory usage: 231.9+ KB
```
Since the column names follow different naming conventions, some of them are renamed. Then dataset is checked for Nan values in inapropriate places and for duplicate rows:
```
S.No             0
Brand_Name       0
Product_ID       0
Product_Name     0
Brand_Desc       0
Product_Size     0
Currancy         0
MRP             13
Sell_Price       0
Discount         0
Category         0
dtype: int64
```

MRP stands for Maximum retail price, so there can be some NaN values in this column. No duplicate columns were found.

After looking at the variations of values in each column, two columns were identified that needed some clean up in order to conduct further analysis:
1) Discount column was transformed to contain only the numerical value of percentage.
2) In Product_Size column 'Size:' prefixes were removed from some rows and 'Nan' string was replaced by NaN value.

### Data Summary

After data preporation, summary of numerical features was obtained:
```
              S.No    Sell_Price     Discount
count  4566.000000   4566.000000  4566.000000
mean   2283.500000   2005.222733    29.991897
std    1318.234994   2259.614915    17.856129
min       1.000000     89.000000     5.000000
25%    1142.250000    749.000000    10.000000
50%    2283.500000   1379.000000    30.000000
75%    3424.750000   2299.000000    50.000000
```
