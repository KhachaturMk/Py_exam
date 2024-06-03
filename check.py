import pandas as pd

inp = input('Request number: ')
try:
    df = pd.read_csv('report.csv')
    df_new = df[df['Request'] == inp]
    print(df_new)
except:
    print('file is empty')