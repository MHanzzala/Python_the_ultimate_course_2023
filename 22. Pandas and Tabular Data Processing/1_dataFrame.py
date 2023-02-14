
import pandas


mydataset = {
    'names': ["Ahmed", "Omar", "Mustafa", "Ali", "Bilal", "hammad"],
    'age': [15, 18, 21, 25, 28, 19],
    'city': ["Lahore", "Multan", "Islamabad", "Lahore", "Multan", "Islamabad"],
    'bikes': ["honda125", "honda70", "yamaha125g", "honda125", "honda70", "yamaha125g"],
    'hobbies': ["cricket", "badminton", "Video Games", "cricket", "badminton", "Video Games"],
    'Phones': ["Samsung S10", "Google Pixel 3", "Xiaomi Note 11", "Samsung S10", "Google Pixel 3", "Xiaomi Note 11"]
}


df = pandas.DataFrame(mydataset)


print(df)


df.to_csv("datafarm_basics.csv", index=False)
