import pandas as pd
import calendar

sales = pd.read_csv(r"C:\Users\WadirMalik\Downloads\BigMartSalesData.csv")

print(sales.head())

print(sales.tail())

sales.info()

print(sales.isnull().values.any())

print(sales.astype({'CustomerID':str}).dtypes)

sales['InvoiceDate'] = pd.to_datetime(sales['InvoiceDate'])
print(sales.dtypes)

sales['Month'] = sales['Month'].apply(lambda x: calendar.month_name[x])
print(sales.head())

print(sales['UnitPrice'].mean())

print(sales['Amount'].max())

totals = sales.groupby('CustomerID')['Amount'].sum()
totals_sorted = totals.sort_values(ascending=False)
print(totals_sorted.head())
print(totals_sorted.tail())

print(sales.groupby('Year').count())

print(sales['CustomerID'].nunique())