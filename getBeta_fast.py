from commonModuleImport import *

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

# return formate

# Period
# Long Term Beta *
# Daily - One Month Range
# Daily - Three Month Range
# Weekly - One Year Range
# Weekly - Two Year Range
# 2 Week - Two Year Range
# Monthly - Two Year Range

def getBeta_fast(COMPANY_NAME):
    url = f'https://www.topstockresearch.com/rt/Stock/{COMPANY_NAME}/BetaAndVolatility'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    table = soup.find_all('tr')
    append_list = []
    itr = 0
    for i in table:
        if(itr>=2):
            break
        for j  in i:
            if(itr>=2):
                break
            if(itr==0):
                continue
            for k in j:
                append_list.append(k)
        itr = itr + 1
    return append_list

# mylist = getBeta_fast('GIRRESORTS')
# print(len(mylist))