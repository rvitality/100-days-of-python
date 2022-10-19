# with open("./weather_data.csv") as data:
#     print(data.readlines())


# import csv

# with open("./weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()

# temp_list = data["temp"].to_list()

# avg_temp = data["temp"].mean()
# max_temp = data["temp"].max()

# print(f"Average temp: {avg_temp}")
# print(f"Max temp: {max_temp}")

# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# monday_temp = float(monday.temp )
# print((monday_temp * 9 / 5) + 32)

data = pandas.read_csv("squirrel_data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

squirrels_count = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(squirrels_count)
df.to_csv("squirrel_count.csv")

# print(gray_squirrels_count)
# print(black_squirrels_count)
# print(white_squirrels_count)
