from commonModuleImport import *

def shareChange(COMPANY_NAME,COMPANY_CSV):
    Day = 0
    previousPrice = 0
    change = 0
    todayPrice = 0
    df = pd.read_csv(COMPANY_CSV)
    fieldnames = ['Date', COMPANY_NAME, COMPANY_NAME+'_change']
    temp_file_path = '/Users/boi_akay/Desktop/Stocks/data.csv'
    with open(temp_file_path, 'a', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for index, row in df.iterrows():
            date = row['Date']
            todayPrice = row['Close']
            if Day>0:
                change = (float(todayPrice)-float(previousPrice))/float(previousPrice)
                # print(date,todayPrice,change)
                previousPrice=todayPrice
            else:
                previousPrice = todayPrice
                Day=Day+1
                # print(date,todayPrice)
            print(f"{COMPANY_NAME} change for {date} : {change}",end='\r')
            # time.sleep(1)
            writer.writerow({'Date': date,COMPANY_NAME:todayPrice,COMPANY_NAME+'_change': change})
    with open(temp_file_path, 'r') as file2:
        file2_contents = file2.read()
    with open(COMPANY_CSV, 'w') as file1:
        file1.write(file2_contents)
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)








