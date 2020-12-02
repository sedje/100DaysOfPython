import pandas


def main():
    # Create a dictionary in this format {"A": "Alfa", "B": "Bravo", etc... }
    nato = pandas.read_csv("nato_phonetic_alphabet.csv")
    alphabet = {row.letter: row.code for (index, row) in nato.iterrows()}

    # Create a list of the phonetic code words from a word that the user inputs.
    name = input("What is your name?: ")
    nato_result = [alphabet.get(letter.upper()) for letter in name]
    print(nato_result)


if __name__ == '__main__':
    main()
