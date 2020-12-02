# import csv
import pandas


def main():
    # with open("weather_data.csv", 'r') as weather_data:
    #     data = csv.reader(weather_data)
    #     temperatures = []
    #     #print(data.line_num)
    #     for row in data:
    #         if row[1].isnumeric():
    #             temperatures.append(int(row[1]))
    #     print(temperatures)
    # data = pandas.read_csv("weather_data.csv")
    # data_dict = data.to_dict()
    # print(data_dict)
    # print(f"Average temp: {data.temp.mean()}")
    # print(f"Max temp: {data.temp.max()}")
    # print(f"Min temp: {data.temp.min()}")
    # print(data[data.temp == data.temp.max()])
    # print(f"The temperature in Fahrenheit is: {to_fahrenheit(data[data.day == 'Monday'].temp)}")
    data_dict = {
        "students":["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data = pandas.DataFrame(data_dict)
    data.to_csv("student_data.csv")

# def to_fahrenheit(temp):
#     return temp * 9/5 + 32
#

if __name__ == "__main__":
    main()
