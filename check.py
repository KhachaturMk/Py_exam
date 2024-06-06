import pandas as pd

# this manual must be installed on the restaurant employee's terminal
# it helps to check order details by unique order number
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