import requests
import smtplib

OWM_weather_api = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = '3646162909cbe91b962ca23cb10ecdfb'

my_email = 'akainetteyephraim10@gmail.com'
password = 'fnsofqbvcmkcbfkc'

weather_parameter = {
    'lat': 5.6037,
    'lon': 0.1870,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(OWM_weather_api, params=weather_parameter)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for hour in weather_data['hourly'][:12]:
    if int(hour['weather'][0]['id']) < 700:
        will_rain = True
        
if will_rain:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject: It's a rainy day\n\nRemember to take your umbrella along, there would be showers :)"
        )

    