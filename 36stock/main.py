import requests
import datetime
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = "AC5ea2a86f7734e0313d354672a1f54722"
TWILIO_AUTH = "092301ed43bba838268e2876b208e0a7"

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "outputsize" : "compact",
    "apikey" : "143HQ71V1ZSN47FL",
    "datatype" : "json"


}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
today = datetime.datetime.now().date()
yesterday = today - datetime.timedelta(days=1)
day_before = today - datetime.timedelta(days=2)

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()
stock_yesterday = float(data["Time Series (Daily)"][f"{yesterday}"]["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price
stock_day_before = float(data["Time Series (Daily)"][f"{day_before}"]["4. close"])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(stock_yesterday - stock_day_before)
up_down = None
if diff > 0:
    up_down = "🔼"
else:
    up_down = "⬇️"


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = round((diff / stock_day_before) * 100)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 1:

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    par_news = {
        "apiKey" : "da7863a5eebe4d1c8b98d6bbc6a3875d",
        "qInTitle" : COMPANY_NAME,
    }

    response_n = requests.get(url=NEWS_ENDPOINT, params=par_news)
    response_n.raise_for_status()

    data2 = response.json()
    article = response_n.json()["articles"]



#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = article[:3]


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}:{up_down}{percentage_difference}%\nHeadline: {article['title']} \nBrief: {article['description']}" for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH)

#TODO 9. - Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+14843034314',
            to='+48509211720'
        )



