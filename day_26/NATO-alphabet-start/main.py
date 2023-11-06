import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)

result = {row.letter: row.code for (index, row) in df.iterrows()}
# print(result)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic_code = [result[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(phonetic_code)


generate_phonetic()
