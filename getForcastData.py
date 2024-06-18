from commonModuleImport import *

def getForcastData(ticker):
    url = f'https://www.tradingview.com/symbols/NSE-{ticker}/forecast/'

    responce  = requests.get(url)
    if (responce.status_code == 200):
        soup = BeautifulSoup(responce.text,'html.parser')
        class1 = 'highlight-maJ2WnzA highlight-Cimg1AIh price-qWcO4bp9'
        soupObject = soup.find(class_=class1)
        if soupObject is None:
            return '####'
        lastPrice = float(soupObject.text.strip()[0:].replace(',',''))
        return lastPrice
    else :
        return '####'