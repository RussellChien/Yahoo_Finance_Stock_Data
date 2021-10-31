import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

class Chart(object):
    def __init__(self, x_length, y_length, title, x_label, y_label, title_font_size, label_font_size, color, linestyle, linewidth):
        self.x_length = x_length
        self.y_length = y_length
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.title_font_size = title_font_size
        self.label_font_size = label_font_size
        self.color = color
        self.linestyle = linestyle
        self.linewidth = linewidth

    def create_chart(self, data):
        data.plot(figsize=(self.x_length,self.y_length))
        plt.legend()
        plt.title(self.title, fontsize=self.title_font_size)
        plt.ylabel(self.x_label, fontsize=self.label_font_size)
        plt.xlabel(self.y_label, fontsize=self.label_font_size)
        plt.grid(which = 'major', color = self.color, linestyle = self.linestyle, linewidth = self.linewidth)
        plt.show()

if __name__ == '__main__':
    addstock = True
    ticker_list = []

    # user input 
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

    # downloading data 
    data = pd.DataFrame(columns=ticker_list)
    for ticker in ticker_list:
        data[ticker] = yf.download(ticker, start=start_date, end=end_date)['Adj Close']

    # creating chart
    adj_close_price = Chart(10, 7, 'Adjusted Close Price', 'Price', 'Year', 16, 14, 'k', '-', .5)
    adj_close_price.create_chart(data)