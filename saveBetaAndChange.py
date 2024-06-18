from commonModuleImport import *
from getBeta_fast import getBeta_fast
from getStockReturns import getStockReturns

finalFilePath = 'data/companyBetaAndChange.csv'
for COMPANY_NAME in validCompaniesNSE:
    betaData = getBeta_fast(COMPANY_NAME)
    if len(betaData) <=0:
        continue
    Long_Term_Beta          = betaData[1]
    Daily_One_Month_Range   = betaData[2]
    Daily_Three_Month_Range = betaData[3]
    Weekly_One_Year_Range   = betaData[4]
    Weekly_Two_Year_Range   = betaData[5]
    two_Week_Two_Year_Range = betaData[6]
    Monthly_Two_Year_Range  = betaData[7]
    oneMonthReturn          = getStockReturns(COMPANY_NAME,'1mo')
    oneYearReturn           = getStockReturns(COMPANY_NAME,'12mo')
    dispTable = PrettyTable(['Company_Name','Long_Term_Beta','Daily_One_Month_Range','1_month_return','12_month_return'])
    dispTable.add_row([f'{COMPANY_NAME}',Long_Term_Beta,Daily_One_Month_Range,oneMonthReturn,oneYearReturn])
    print(dispTable)

    tempDF = pd.read_csv(finalFilePath)
    if COMPANY_NAME in tempDF['Company_Name'].values:
        print(Akaycolours.RED+f'{COMPANY_NAME} is already present'+Akaycolours.RESET)
        tempDF = tempDF[tempDF['Company_Name'] != COMPANY_NAME]
        tempDF.to_csv(finalFilePath,index=False)
    
    with open(finalFilePath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([COMPANY_NAME, Long_Term_Beta, Daily_One_Month_Range,Daily_Three_Month_Range, Weekly_One_Year_Range ,Weekly_Two_Year_Range,two_Week_Two_Year_Range,Monthly_Two_Year_Range,oneMonthReturn,oneYearReturn])
    
    df = pd.read_csv(finalFilePath)
    df = df.sort_values(by='1_month_return')
    df.to_csv(finalFilePath,index=False)