import pandas as pd
df = pd.read_csv('music_log.csv')
#theory

cholera = pd.read_csv('cholera.csv')
cholera.info()
print(cholera.isnull().sum())
print(cholera.isna().sum())
cholera['imported_cases']=cholera['imported_cases'].fillna(0)
print(cholera.isna().sum())
cholera.dropna(subset=['total_cases','deaths','case_fatality_rate'],inplace=True)
print(cholera)

#practice
new_names = ['user_id',
             'total_play_seconds',
             'artist_name',
             'genre_name',
             'track_name'
             ]
#print(new_names)
df.set_axis(new_names,axis='columns',inplace=True)

#print(df.columns)
#print(df.head(10))