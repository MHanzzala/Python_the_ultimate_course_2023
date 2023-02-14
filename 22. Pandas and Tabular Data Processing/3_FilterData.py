import pandas as pd
from IPython.display import display

df = pd.read_csv(
    "/home/hanzala/Development/Python_the_ultimate_course_2023/22. Pandas and Tabular Data Processing/datafarm_basics.csv")


pd.set_option("display.max_rows", None)  # showall

display(df)


print("================================")

filterCity = df.loc[df['city'] == 'Lahore']

display(filterCity)

print("================================")

filterBikes = df.loc[df['bikes'] == 'honda125']

display(filterBikes)

print("================================")
filterProductInLahore = df.loc[(
    df['bikes'] == 'honda125') & (df['city'] == 'Lahore')]

display(filterProductInLahore)

print('--------------------------------')
ageTotal = filterProductInLahore['age'].sum()

print("Total age of filter items:", ageTotal)
