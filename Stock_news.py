import requests
from datetime import datetime, timedelta
import pandas as pd

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_kEY = "UNF3ISGZRQPCRK5E"

Parameter = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_kEY,
}
response = requests.get(url = STOCK_ENDPOINT,params=Parameter)
data = response.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_stock_price = data_list[0]['4. close']

# Another way using datetime libraray
# YESTERDAY_DATE = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
# yesterday_closing_price = response.json()["Time Series (Daily)"][YESTERDAY_DATE]["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_stock_price = data_list[1]["4. close"]

difference_between_price = float(yesterday_stock_price)-float(day_before_yesterday_closing_stock_price)
positive_difference_between_price = abs(difference_between_price)
print(positive_difference_between_price)
up_down = None
if difference_between_price<0:
    up_down = "📉"
else:
    up_down = "📈"

percentage_difference = (difference_between_price/float(day_before_yesterday_closing_stock_price))*100
print(percentage_difference)

if(abs(percentage_difference)>5):
    print("Get News")

NEWS_API_KEY = 'cf043ff266cd4dbe9f9394682eb5f466'
news_parameretr = {
    'qInTitle': STOCK_NAME,
    'apikey': NEWS_API_KEY,
    'language': 'en',
}
new_data = requests.get(url = "https://newsapi.org/v2/everything", params=news_parameretr)
Articles = new_data.json()["articles"]
if len(Articles)>3:
    news_content = Articles[:3]
else:
    news_content = Articles[:len(Articles)]

content = [f"{STOCK_NAME}: {up_down} {abs(percentage_difference)}%\nHeadline: {dict['title']}. \nBrief: {dict['description']} \nURL: {dict['url']}\n" for dict in news_content ]
print(content[0])

from twilio.rest import Client
# and set the environment variables. See http://twil.io/secure
account_sid = "AC9bdcaad187aea00918f9fadf9ab6dcab"
auth_token = '6f565973659e6ace25efc89f7e8953b5'
client = Client(account_sid, auth_token)
for info in content:
    message = client.messages.create(
                     body=info,
                     from_='+13254406649',
                     to='+918529774150'
                 )
    print(info)
    print("Message sent")