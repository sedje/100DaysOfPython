# Print only squared result from numbers list
def squaring():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [num**2 for num in numbers]
    print(f"Squared numbers: {squared_numbers}")


# Print only even numbers from numbers list
def filter_even():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Even numbers: {even_numbers}")


# Print only overlapping numbers from two numbers lists
def data_overlap():
    with open("file1.txt") as file1:
        list1 = file1.readlines()
    with open("file2.txt") as file2:
        list2 = file2.readlines()

    overlap = [int(num) for num in list1 if num in list2]
    print(f"Overlapping values: {overlap}")


if __name__ == '__main__':
    squaring()
    filter_even()
    data_overlap()