# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

letter_df = pandas.read_csv('nato_phonetic_alphabet.csv')
letter_dict = {row.letter: row.code for (index, row) in letter_df.iterrows()}



def create_list():    
    user_word = input("Enter a word: ").upper()
    user_list = [letter_dict[letter] for letter in user_word]
    return user_list

check = True

while check:
    try:   
        print(create_list())
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        check = False
    


   


    