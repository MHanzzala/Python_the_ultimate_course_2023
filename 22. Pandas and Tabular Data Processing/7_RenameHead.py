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

print("Results after Renamed Header")

print("================================")

df = df.rename({'names': 'FirstName'}, axis=1)
df = df.rename({'bikes': 'MotorCycle'}, axis=1)

display(df)
