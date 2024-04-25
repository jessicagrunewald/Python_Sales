# importing pandas to work with Excel
import pandas as pd

# importing the database
db_sales = pd.read_excel('Sales.xlsx')

# visualization of database data
pd.set_option('display.max_columns', None)
