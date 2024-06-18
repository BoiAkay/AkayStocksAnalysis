from datetime import datetime
import yfinance as yf
import Akaycolours



def downloadStockData(ticker,downloadPath):
    startDate = '2021-01-01'
    todayDate = datetime.today().strftime('%Y-%m-%d')
    data = yf.download(ticker, start=startDate, end=todayDate)
    if data.empty:
        return 0
    # print(data.head())
    # data = data['Close']
    data.to_csv(downloadPath)
    print(Akaycolours.BLUE+f'file saved at {downloadPath}'+Akaycolours.RESET)
    return 1
