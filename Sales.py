# importing pandas to work with Excel
import pandas as pd

# importing the database
db_sales = pd.read_excel('Sales.xlsx')

# visualization of database data
pd.set_option('display.max_columns', None)

# revenue per store
# filtering 'ID Loja' and 'Valor Final' columns and group data by store
revenue = db_sales[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
