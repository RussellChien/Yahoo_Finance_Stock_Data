import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

class yfinance_adjusted_closing_price(object):
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

if __name__ == '__main__':
    addstock = True
    ticker_list = []
    while (addstock) :
        ticker = input('What stock(s) would you like to get market data on? Enter "done" when done entering tickers. ')
        ticker = ticker.upper()
        if (ticker == 'DONE'):
            addstock = False
        else:
            ticker_list.append(ticker)

    date_range = input('Please enter a date range with the format YYYY-MM-DD,YYYY-MM-DD: ')
    start_date = date_range[:10]
    end_date = date_range[11:]
    # data = yf.download(ticker, start_date, end_date)
    data = pd.DataFrame(columns=ticker_list)

    for ticker in ticker_list:
        data[ticker] = yf.download(ticker, start_date, end_date)['Adj Close']

    data.head()
    data.plot(figsize=(10,7))
    plt.legend()
    # plt.title('Adjusted Close Price of %s' %ticker.upper(), fontsize=16)
    plt.title('Adjusted Close Price', fontsize = 16)
    plt.ylabel('Price', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.grid(which = 'major', color = 'k', linestyle = '-', linewidth = .5)
    plt.show()
