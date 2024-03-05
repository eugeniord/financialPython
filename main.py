# main.py
from app.playground import test1, getnPlotClosingPrices1Y, getData
from datetime import datetime

def main():
    now = datetime.now()
    test1('AAPL')
    #getnPlotClosingPrices1Y('AAPL', '2023-03-05', now )
    getData('AAPL')

if __name__ == "__main__":
    main()
