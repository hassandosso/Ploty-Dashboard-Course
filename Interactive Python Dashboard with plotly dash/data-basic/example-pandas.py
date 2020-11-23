import pandas as pd
df= pd.read_csv('salary_data.csv')
ser_log = df['Salary'] > 100000
#print(df[ser_log])
print(df.info())
print(df.describe())
print(df.isna().sum())