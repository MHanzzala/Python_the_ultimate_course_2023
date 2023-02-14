import pandas as pd
from IPython.display import display

df = pd.read_csv(
    "/home/hanzala/Development/Python_the_ultimate_course_2023/22. Pandas and Tabular Data Processing/datafarm_basics.csv")


pd.set_option("display.max_rows", None)  # showall

display(df)

print('--------------------------------')

ageTotal = df['age'].sum()

print("Total age of filter items:", ageTotal)
