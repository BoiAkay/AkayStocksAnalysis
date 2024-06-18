from commonModuleImport import *
from findChange import shareChange

def deleteFaltuColoums(file_path):
    df1 = pd.read_csv(file_path)

    columns_to_remove = ['Open', 'High','Low','Adj Close','Volume']
    df1.drop(columns=columns_to_remove, inplace=True)
    df1 = df1.sort_values(by=df1.columns[0])
    df1.to_csv(file_path,index=False)

def fill_null_with_last(df):
    return df.ffill()

def replaceNULL(input_file):
    df = pd.read_csv(input_file)
    df_filled = fill_null_with_last(df)
    df_filled.to_csv(input_file, index=False)


def mergeFiles(NIFTY_CSV,COMPANY_CSV,MERGED_FILE_PATH,COMPANY_NAME,NIFTY_NAME):

    df1 = pd.read_csv(NIFTY_CSV)
    df2 = pd.read_csv(COMPANY_CSV)

    if(len(df1)!=len(df2)):
        print(Akaycolours.RED+f'[ERROR] {NIFTY_NAME} len = {len(df1)} {COMPANY_NAME} len = {len(df2)}'+Akaycolours.RESET)
        # sys.exit("Exiting the code!")
        return 0

    deleteFaltuColoums(NIFTY_CSV)
    deleteFaltuColoums(COMPANY_CSV)

    replaceNULL(COMPANY_CSV)
    replaceNULL(NIFTY_CSV)

    
    shareChange(COMPANY_NAME,COMPANY_CSV)
    shareChange(NIFTY_NAME,NIFTY_CSV)

    df1 = pd.read_csv(NIFTY_CSV)
    df2 = pd.read_csv(COMPANY_CSV)

    merged_df = pd.merge(df2, df1, on='Date', how='outer') # check you dataset for the first coloum
    merged_df = merged_df.sort_values(by=merged_df.columns[0])
    merged_df.to_csv(MERGED_FILE_PATH, index=False)
    return 1

