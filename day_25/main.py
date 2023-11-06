# # import csv
import pandas as pd

# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     header = next(data)
# #     temperatures = []
# #     for row in data:
# #         temperatures.append(int(row[1]))

# #     print(temperatures)


# 

# data = pd.read_csv("weather_data.csv")
# # print(data['temp'])

# # data_dict = data.to_dict()
# # print(data_dict)

# data_list = data["temp"].to_list()
# # print(data_list)

# # sum = 0
# # for temp in data_list:
# #     sum += temp

# # print(f"Average temperature is: {sum/len(data_list)}")

# avg_temp = sum(data_list) / len(data_list)
# # print(f"Average temperature is: {avg_temp}")

# # print(data["temp"].max())

# # get data in columns
# # print(data["condition"])
# # print(data.condition)

# # get data in row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# # print(monday_temp)
# c_to_f = monday_temp * 9/5  + 32
# print(c_to_f)


# # create a dataframe from scratch
# data_dict = {
#     "students": ["Manisha", "Vidisha", "Monika", "Kshitija", "Prachi"],
#     "scores": [90, 98, 88, 97, 67]
# }
# data1 = pd.DataFrame(data_dict)
# # print(data1)
# data1.to_csv("new_data.csv")

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231012.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(red_squirrels_count)
# print(black_squirrels_count)

data_dict = {
    "Furr Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data = pd.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
