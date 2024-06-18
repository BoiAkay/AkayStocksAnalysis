# url1 = 'https://www.google.com/finance/quote/ZOMATO:NSE&window=MAX'
# url2 = 'https://www.google.com/finance/quote/543320:BOM'

from commonModuleImport import *

def realTimeStockData(COMPANY_NAME):
    url = f'https://www.google.com/finance/quote/{COMPANY_NAME}:NSE'
    responce  = requests.get(url)
    if (responce.status_code == 200):
        class1 = 'YMlKec fxKbKc'
        soup = BeautifulSoup(responce.text,'html.parser')
        soupObject = soup.find(class_=class1)
        if soupObject is None:
            return '####'
        class1 = 'YMlKec fxKbKc'
        lastPrice = float(soupObject.text.strip()[1:].replace(',',''))
        return lastPrice
    else:
        return '####'

lastPrice = realTimeStockData('JIOFIN')
print(lastPrice)