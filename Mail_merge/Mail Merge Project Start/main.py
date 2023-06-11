with open('./Input/Letters/starting_letter.txt') as starting_letter:
    letter = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

for name in names:
    new_name = name.strip("\n")
    finished_letter = letter.replace('[name]', new_name)
    with open(f'./Output/ReadyToSend/letter_for_{new_name}.txt', mode="w") as new_letter:
        new_letter.write(finished_letter)



