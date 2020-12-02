import pandas


def main():
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    fur_data = data.value_counts("Primary Fur Color")
    fur_data.to_csv("squirrel_count.csv")


if __name__ == '__main__':
    main()
