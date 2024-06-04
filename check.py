import pandas as pd

inp = input('Request number: ')
try:
    df = pd.read_csv('report.csv')
    df_new = df[df['Request'] == inp]
    if df_new.empty:
        print('Request not found')
    else:
        print(df_new)
except:
    print('File is empty')