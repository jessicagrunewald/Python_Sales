# importing pandas to work with Excel
import pandas as pd

import datetime

# importing the database
db_sales = pd.read_excel('Sales.xlsx')

# visualization of database data
pd.set_option('display.max_columns', None)

# extracting the month from the date column and adding this value in a new column named "Mês"
db_sales['Data'] = pd.to_datetime(db_sales['Data'], format='%d/%m/%Y')
db_sales['Mês'] = db_sales['Data'].dt.month

# revenue per store
# filtering 'ID Loja' and 'Valor Final' columns and group data by store
revenue = db_sales[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

# revenue per month
# filtering 'Mês' and 'Valor Final' columns and group data by store
revenue_month = db_sales[['Mês', 'Valor Final']].groupby('Mês').sum()

# Top 5 stores with the highest revenue in the year
highest_revenue = db_sales[['ID Loja', 'Valor Final']].groupby('ID Loja').sum().sort_values(by='Valor Final', ascending=False).head(5)

# Top 5 stores with the lowest revenue in the year
lower_revenue = db_sales[['ID Loja', 'Valor Final']].groupby('ID Loja').sum().sort_values(by='Valor Final').head(5)

# quantity of product sold per store
# filtering 'ID Loja' and 'Quantidade' columns and group data by store
quantity_product = db_sales[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

# quantity of product sold per month
# filtering 'Mês' and 'Quantidade' columns and group data by store
quantity_product_month = db_sales[['Mês', 'Quantidade']].groupby('Mês').sum()

# average ticket per product in each store
average_ticket = (revenue['Valor Final'] / quantity_product['Quantidade']).to_frame()

# average ticket per product in each month
average_ticket_month = (revenue_month['Valor Final'] / quantity_product_month['Quantidade']).to_frame()

