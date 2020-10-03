import pandas as pd

url="https://paycheck.in/salary/minimumwages/maharashtra/maharashtra-minimum-wages-w-e-f-january-1-2014-to-june-30-2014"
table = pd.read_html(url)[0]
table.to_excel("sheet.xlsx")