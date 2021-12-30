import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_list = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_data_list)

{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
game_on = True
while game_on:
    user_word = input("Enter a word: ").upper()
    user_nato_list = [nato_data_list[letter] for letter in user_word]
    print(user_nato_list)
    more_word = input("More word? 'y' or 'n' ").lower()
    if more_word == "n":
        game_on = False
