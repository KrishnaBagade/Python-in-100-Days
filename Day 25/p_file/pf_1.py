# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv",mode="r") as file:
#      data = csv.reader(file)
#      temperature = []
#      for row in data:
#          if row[1].isdigit():
#            temperature.append(int(row[1]))
# print(temperature)

import pandas
# gray = 0
# nan = 0
# cinnamon = 0
# black = 0
# data = pandas.read_csv("weather_data.csv")
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # print(squirrel_data.columns.values.tolist())
# # print(squirrel_data['Primary Fur Color'].unique())
# for squirrel in range(len(squirrel_data)-1):
#     if squirrel_data['Primary Fur Color'][squirrel] == "Gray":
#         gray += 1
#     if squirrel_data['Primary Fur Color'][squirrel] == "Cinnamon":
#         cinnamon += 1
#     if squirrel_data['Primary Fur Color'][squirrel] == "Black":
#         black += 1
# nan = squirrel_data['Primary Fur Color'].isna().sum()
# # print(gray,cinnamon,nan,black)
# fur_data = {"Fur Color":["Gray","Red","Black","Unknown"],
#             "Count":[f"{gray}",f"{cinnamon}",f"{black}",f"{nan}"]}
# squirrel_data_color_data = pandas.DataFrame.from_dict(fur_data)
# squirrel_data_color_data.to_csv("Squirrel_Count.csv")