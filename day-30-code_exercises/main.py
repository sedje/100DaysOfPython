import pandas


def index_errors():
    fruits = ["Apple", "Pear", "Orange"]

    # TODO: Catch the exception and make sure the code runs without crashing.
    def make_pie(index):
        try:
            fruit = fruits[index]
        except IndexError:
            print("Fruit pie")
        else:
            print(fruit + " pie")

    make_pie(1)
    make_pie(2)

    make_pie(4)


def key_errors():
    facebook_posts = [
        {'Likes': 21, 'Comments': 2},
        {'Likes': 13, 'Comments': 2, 'Shares': 1},
        {'Likes': 33, 'Comments': 8, 'Shares': 3},
        {'Comments': 4, 'Shares': 2},
        {'Comments': 1, 'Shares': 1},
        {'Likes': 19, 'Comments': 3}
    ]

    total_likes = 0

    for post in facebook_posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass

    print(total_likes)


def nato_alphabet():
    # Keyword Method with iterrows()
    # {new_key:new_value for (index, row) in df.iterrows()}
    try:
        data = pandas.read_csv("nato_phonetic_alphabet.csv")
    except FileNotFoundError:
        print("No alphabet found!")
    else:
        # Create a dictionary in this format {'A': 'Alpha', 'B', 'Bravo', etc... }:
        phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
        print(phonetic_dict)
    generate_phonetic(phonetic_dict)


def generate_phonetic(phonetic_dict):
    # Create a list of the phonetic code words from a word that the user inputs.
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic(phonetic_dict)
    else:
        print(output_list)


if __name__ == '__main__':
    # index_errors()
    # key_errors()
    nato_alphabet()
