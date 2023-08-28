import requests
from datetime import datetime, timedelta
import pandas


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key_alpha = ' GOP2ERI734J12562'
news_api_key = 'd3041e0392894223a785cc7d91022262'

parameters_alpha = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': api_key_alpha
}

parameters_news = {
    'apiKey': news_api_key,
    'q': 'Tesla',
    'category': 'business',
    'country':'us'
}

url_alpha = 'https://www.alphavantage.co/query'
url_news = 'https://newsapi.org/v2/top-headlines'


response = requests.get(url=url_alpha, params=parameters_alpha)
data = response.json()

previous_week_days = []
today = datetime.today()

for i in range(7):
    d = today - timedelta(days=i)
    if d.weekday() < 5:            
        previous_week_days.append(f"{d.date()}")

print(previous_week_days)

days_1 =previous_week_days[1]
days_2 = previous_week_days[2]

days_1_data = data['Time Series (Daily)'][f"{days_1}"]
days_2_data = data['Time Series (Daily)'][f"{days_2}"]

#alternative
data_list = [value for (key, value) in data['Time Series (Daily)'].items()]
print(data_list)

close_1 = float(days_1_data['4. close'])
close_2 = float(days_2_data['4. close'])
print(close_1, close_2)



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
if ((close_1-close_2)/close_2) > 0.05 or ((close_2-close_1)/close_2) > 0.05:
    print('Get News')

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_response = requests.get(url=url_news, params=parameters_news)
    news_data = news_response.json()['articles']
    relevant_news = news_data[:3]
    print(relevant_news[0]['content'])
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

