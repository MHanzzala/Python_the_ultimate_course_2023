import pandas as pd
from IPython.display import display
pd.set_option("display.max_row", None)
df = pd.read_csv(
    "/home/hanzala/Development/Python_the_ultimate_course_2023/22. Pandas and Tabular Data Processing/datafarm_basics.csv")


# to display the correct results we use display on datraframes not print because it give us the
# crroupt dataframe.....
# print(df)
print("\n================================")
display(df)


print("\n================================")

print("Results after Date Filtering:")

print("================================")

df['Date'] = pd.to_datetime(df['Date'])
date_1 = pd.to_datetime('1/1/2020')
date_2 = pd.to_datetime('30/12/2020')

filterDate = df[df.Date.between(date_1, date_2)]

display(filterDate)