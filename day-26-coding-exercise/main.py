from random import randint
import pandas


def explanations1():
    # List comprehension, create a list from a list
    numbers = [1, 2, 3]
    new_num = [num+1 for num in numbers]
    print(new_num)

    # Iterate through a name character by character and convert into a list
    name = "Anko"
    name_list = [char for char in name]
    print(name_list)

    # Conditions in list comprehension
    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]
    # Only add names if length is less than 5
    short_names = [name for name in names if len(name) < 5]
    print(short_names)


def explanations2():
    # new_dict = { new_key:new_value for (key, value) in dict.items() if test }
    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]
    student_scores = {name: randint(1, 100) for name in names}
    print(student_scores)

    passed_students = {name: score for (name, score) in student_scores.items() if score >= 55}
    print(passed_students)

    student_dict = {
        "student": ["Angela", "James", "Lily"],
        "score": [56, 76, 98]
    }
    student_data_frame = pandas.DataFrame(student_dict)

    # 'old' way of iterating through rows.
    for (key, value) in student_data_frame.items():
        print(value)
    # Pandas way of iterating through rows
    for (index, row) in student_data_frame.iterrows():
        # print all names
        print(row.student)
        # print all scores
        print(row.score)
        # print only score of student 'Angela'
        if row.student == "Angela":
            print(row.score)


def challenge_1():
    # Create a list where range(1,5) returns values * 2
    range_list = [num*2 for num in range(1, 5)]
    print(range_list)


def challenge_2():
    # Create a list of uppercase names for names longer than 5 characters
    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]
    long_names = [name.upper() for name in names if len(name) > 5]
    print(long_names)


def challenge3():
    # Use dict comprehension to create a dict with words and their length from a sentence
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    words = {word: len(word) for word in sentence.split()}
    print(words)


def challenge4():
    # Use dictionary comprehension to convert a list of Celsius temps to Fahrenheit
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }
    # (temp_c * 9/5) + 32 = temp_f
    weather_f = {day: (temp * 9/5 + 32) for (day, temp) in weather_c.items() }
    print(weather_f)


if __name__ == '__main__':
    # explanations1()
    # challenge_1()
    # challenge_2()
    # Dictionary comprehension
    explanations2()
    challenge3()
    challenge4()