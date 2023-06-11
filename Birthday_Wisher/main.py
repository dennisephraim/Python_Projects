import smtplib
import datetime as dt
import random

my_email = 'akainetteyephraim10@gmail.com'
password = 'fnsofqbvcmkcbfkc'



with open('quotes.txt', 'r') as data:
    quotes = data.readlines()

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr= my_email, 
            to_addrs= 'akainetteyephraim@yahoo.com', 
            msg= f"Subject:Weekly Motivational Quote\n\n{random.choice(quotes)}")