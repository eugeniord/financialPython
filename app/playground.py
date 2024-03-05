import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def test1(stockName):
    ticker = yf.Ticker(stockName)
    todays_data = ticker.history(period='1d')
    print(todays_data)

def getnPlotClosingPrices1Y(stockName, start_date, end_date, interval='1d'):
    data = yf.download(stockName, start=start_date, end=end_date, interval=interval)

    if data.empty:
        print("No data found for the given ticker symbol and date range.")
        return
    
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 6))

    plt.plot(data.index, data['Close'], label='Close Price', color='tab:blue', linewidth=2.5)

    # Expressive plot 
    plt.title(f"{stockName} Stock Price ({start_date} to {end_date})", fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Close Price (USD)', fontsize=14)
    plt.legend()
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    plt.tight_layout()
    plt.show()

def getData(stockName):
    ticker = yf.Ticker(stockName)
    list(ticker)

class MyClass:
    def __init__(self):
        print('Hi')