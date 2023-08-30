import smtplib
import json

my_email = 'your_email'
password = 'your_password'

with open("Mail_Merge_Project/Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

with open("Mail_Merge_Project/Input/Names/invited_names.json", 'r') as invited_names:
    names = json.load(invited_names)
    

for name, info in names.items():
    finished_letter = letter.replace('[name]', name)
    with open(f'Mail_Merge_Project/Output/ReadyToSend/letter_for_{name}.txt', mode="w") as new_letter:
        new_letter.write(finished_letter)

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=info['email'],
            msg=f"Subject: Birthday Invitation!\n\n{finished_letter}"
        )
