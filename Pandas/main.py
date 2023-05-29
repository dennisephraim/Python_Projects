# # with open('weather_data.csv') as data:
# #     data = data.readlines()

# # print(data, type(data))

# # import csv

# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []

# #     for row in data:
# #         if row[1] == 'temp':
# #             pass
# #         else:
# #             temperatures.append(int(row[1]))
        
# #     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# # print(data)

# average = data['temp'].mean()
# # print(average)
# # print(data[data.temp == data.temp.max()])

# monday = data[data.day == "monday"]
# print(monday)


data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

black_count = 0
gray_count = 0
cinnamon_count = 0

pri_color = data['Primary Fur Color']
pri_color_list = pri_color.to_list()

for element in pri_color_list:
    if element == "Black":
        black_count += 1
    elif element == "Gray":
        gray_count += 1
    elif element == "Cinnamon":
        cinnamon_count += 1

dict_data = {'Fur Color': ['Black', 'Gray', 'Cinnamon'],
             'Count': [f'{black_count}', f'{gray_count}', f'{cinnamon_count}']}

new_df = pandas.DataFrame(dict_data)
new_df.to_csv('Squirrel_Count')