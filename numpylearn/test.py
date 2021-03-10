import pandas as pd
import numpy as np

s = pd.Series([-1.10, 2, -3.33, 4])
print(s)
df = pd.DataFrame(s)
print(df)


# Create a Pandas dataframe from some data.
df = pd.DataFrame({
    'Country':    ['China',    'India',    'United States', 'Indonesia'],
    'Population': [1404338840, 1366938189, 330267887,       269603400],
    'Rank':       [1,          2,          3,               4]})

# Order the columns if necessary.
df = df[['Rank', 'Country', 'Population']]

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_table.xlsx', engine='xlsxwriter')

# Write the dataframe data to XlsxWriter. Turn off the default header and
# index and skip one row to allow us to insert a user defined header.
df.to_excel(writer, sheet_name='Sheet2', startrow=1, header=False, index=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets['Sheet2']
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(type(worksheet))
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# Get the dimensions of the dataframe.
(max_row, max_col) = df.shape

# Create a list of column headers, to use in add_table().
column_settings = [{'header': column} for column in df.columns]

# Add the Excel table structure. Pandas will add the data.
worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})

# Make the columns wider for clarity.
worksheet.set_column(0, max_col - 1, 12)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

