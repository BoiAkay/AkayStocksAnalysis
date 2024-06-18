from commonModuleImport import *


# input
# company name
# timePeriod = 12mo or 1mo
def getStockReturns(COMPANY_NAME,timePeriod):
    tickerCompany = f'{COMPANY_NAME}.NS'
    company = yf.Ticker(tickerCompany)
    hist = company.history(period=timePeriod)
    try:
        startPrice = hist[['Close']].iloc[0]['Close']
    except:
        return sys.maxsize
    lastPrice = hist[['Close']].iloc[-1]['Close']
    stockReturn = (lastPrice - startPrice)/startPrice
    stockReturn = stockReturn*100
    return stockReturn