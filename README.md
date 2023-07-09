# Stock_News_alert
<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1>Stock Analysis</h1>
  <p>This repository contains a Python script for analyzing stock data and sending relevant news updates.</p>
  
  <h2>Overview</h2>
  <p>Hello!! I created this Stock News Alert Project. The script retrieves daily stock data for Tesla Inc (TSLA) using the Alpha Vantage API. It calculates the difference in stock prices between yesterday and the day before yesterday, determines the percentage difference, and checks if it exceeds 5%. If the difference is significant, it retrieves news articles related to Tesla from the News API.</p>
  
  <h2>Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>Requests library</li>
    <li>Pandas library</li>
    <li>Twilio library</li>
    <li>Alpha Vantage API key</li>
    <li>News API key</li>
    <li>Twilio account credentials</li>
  </ul>
  
  <h2>Usage</h2>
  <ol>
    <li>Replace the placeholders in the code with your API keys, Twilio credentials, and desired phone numbers.</li>
    <li>Run the script in a Python environment.</li>
    <li>The script will retrieve the stock data, calculate the price difference, and check for significant changes.</li>
    <li>If significant changes are detected, it will fetch news articles related to Tesla.</li>
    <li>The script will send SMS messages with the relevant information using Twilio.</li>
  </ol>
  
  
</body>
</html>
