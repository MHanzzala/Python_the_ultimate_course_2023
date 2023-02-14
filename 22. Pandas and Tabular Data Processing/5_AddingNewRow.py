import pandas as pd
from IPython.display import display
pd.set_option("display.max_row", None)
df = pd.read_csv(
    "/home/hanzala/Development/Python_the_ultimate_course_2023/22. Pandas and Tabular Data Processing/datafarm_basics.csv")


# to display the correct results we use display on datraframes not print because it give us the
# crroupt dataframe.....
# print(df)

display(df)

newEntry = {'names': 'Hanzala',
            'age': 24,
            'city': 'Karachi',
            'bikes': 'honda70',
            'hobbies': 'Video Games',
            'Phones': 'Google Pixel 4'}

df.append(newEntry, ignore_index=True)

df.to_csv("new_datafarm_basics.csv")
