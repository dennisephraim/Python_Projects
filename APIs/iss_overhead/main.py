import requests
from datetime import datetime
import smtplib
import time

my_email = 'akainetteyephraim10@gmail.com'
password = 'fnsofqbvcmkcbfkc'

MY_LAT = 5.6037
MY_LNG = 0.1870

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()
data = response.json()

longitude = float(data['iss_position']['longitude'])
latitude = float(data['iss_position']['latitude'])

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}


response_1 = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response_1.raise_for_status()
data = response_1.json()

sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
time_now = datetime.now().hour


def iss_within():
    if MY_LAT-5 <= latitude <= MY_LAT+5:
        if MY_LNG-5 <= latitude <= MY_LNG+5:    
            return True
        else:
            return False
    else:
        return False
    
def sendmail():
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg='Subject: The ISS is Over You!\n\nGo out and look up to see the ISS!'
            )
    
def check():
    print(iss_within())
    print(longitude, latitude)
    print(time_now, sunset)
    if iss_within():
        if time_now == sunset:
             sendmail()
    time.sleep(5)
    check()
    
    

check() 
