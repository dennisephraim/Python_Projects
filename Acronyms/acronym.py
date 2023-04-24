user_data = input("Please enter the words for the acronym: ").split()
acr_name = ""
for word in user_data: 
    acr_name += word[0]

print(acr_name.upper())