import pandas as pd

# Read the CSV file
df = pd.read_csv(r'C:\Users\User\Desktop\DjangoVSCode\RotaractProject\rotaract.csv')

df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])

df['start_date'] = df['start_date'].dt.date
df['end_date'] = df['end_date'].dt.date

print(df.head())

df.to_csv(r'C:\Users\User\Desktop\DjangoVSCode\RotaractProject\rotaract_.csv', index=False)
