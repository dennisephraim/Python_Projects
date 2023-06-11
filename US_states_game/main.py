import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# print(data['temp'].max())

# print(data.condition)

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# temp_far = (int(monday.temp) * 1.8) + 32
# print(temp_far)


squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = squirrel_data["Primary Fur Color"]
s_count = pandas.DataFrame(fur_color.value_counts())

sd = s_count.to_dict()
print(sd)
s_data = {
    "fur Color": ['gray', 'red', 'black'],
    "count": [sd['Primary Fur Color']['Gray'], sd['Primary Fur Color']['Cinnamon'], sd['Primary Fur Color']['Black']]
}

squirrel_d = pandas.DataFrame(s_data)
squirrel_d.to_csv("Squirrel_count")