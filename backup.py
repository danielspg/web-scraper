

"""


THIS script will crawl the NSE.com and store the values of following stock
RELIANCE , SBIN, ASIANPAINT, TATAMOTORS, CIPLA

We will be storing the current price of these stocks in



in the "STOCK_result.csv" file.

the script will run for 30 minutes.
and the updated value of stock is recorded every 30 seconds.

"""



import sys
import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import date
from datetime import datetime

filename = "STOCK_result.csv"
f = open(filename, 'w')
headers = "RELIANCE , SBIN, ASIANPAINT, TATAMOTORS,CIPLA \n"

f.write(headers)


def fetch_NSE_stock_price(stock_code):
    stock_url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=' + str(
        stock_code)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(stock_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_array = soup.find(id='responseDiv').getText().strip().split(":")
    for item in data_array:
        if 'lastPrice' in item:
            index = data_array.index(item) + 1
            latestPrice = data_array[index].split('"')[1]
            return float(latestPrice.replace(',', ''))


## MAIN
## Usage of programe
## python <programe name> <stock code> <number of pol or iteratio> <at time interval in seconds>
## For example : python NSEStock_saveStock2CSV SBIN 10 5
## Above command will save 10 SBI stock price polled at interval of 5 seconds

# stock_code = sys.argv[1]
# t_iteration = int(sys.argv[2])
# d_sleep = int(sys.argv[3])


stock_code1 = "RELIANCE"
stock_code2 = "SBIN"
stock_code3 = "ASIANPAINT"
stock_code4 = "TATAMOTORS"
stock_code5 = "CIPLA"




t_iteration = 1000 #number of
d_sleep = 2

# data_file = open(stock_code + '_NSE_stock.csv', 'w');

iteration = 0
while iteration < t_iteration:
    # c_date = date.today().strftime("%B %d, %Y")
    # c_time = datetime.now().strftime("%H:%M:%S")
    current_stock_price1 = fetch_NSE_stock_price(stock_code1)
    current_stock_price2 = fetch_NSE_stock_price(stock_code2)
    current_stock_price3 = fetch_NSE_stock_price(stock_code3)
    current_stock_price4 = fetch_NSE_stock_price(stock_code4)
    current_stock_price5 = fetch_NSE_stock_price(stock_code5)
    # print(stock_code + ',' + c_date + ',' + c_time + ',' + str(current_stock_price))
    # print(stock_code + ',' + c_date + ',' + c_time + ',' + str(current_stock_price), file=data_file)
    print(str(current_stock_price1) + ',' + str(current_stock_price2) + ',' + str(current_stock_price3) + ',' + str(current_stock_price4)+ ',' + str(current_stock_price5), file=f)
    time.sleep(d_sleep)
    iteration = iteration + 1

f.close()

# End
