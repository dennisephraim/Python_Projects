import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


user_text = input("Enter the word: ").upper()
user_text_list = list(user_text)

nato_list = [nato_dict[letter] for letter in user_text_list if letter in nato_dict]
print(nato_list)

