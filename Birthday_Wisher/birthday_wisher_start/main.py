import pandas
import smtplib
import datetime as dt
import random

my_email = 'akainetteyephraim10@gmail.com'
password = 'fnsofqbvcmkcbfkc'

birthdays = pandas.read_csv('birthdays.csv')
current_date = dt.datetime.now()
month_borns = birthdays[birthdays.month == current_date.month]
current_birthdays = month_borns[month_borns.day == current_date.day]

for index, row in current_birthdays.iterrows():
    with open(f'letter_templates/letter_{random.randint(1, 3)}.txt', 'r') as text:
        letter = text.read()

    bday_letter = letter.replace('[NAME]', row['name'])
    print(bday_letter)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=row['email'], 
            msg=f"Subject: Happy Birthday!\n\n{bday_letter}")



