import pandas as pd
df = pd.read_csv('music_log.csv')
#theory

cholera = pd.read_csv('cholera.csv')

#print(cholera.isnull().sum())
#print(cholera.isna().sum())
cholera['imported_cases']=cholera['imported_cases'].fillna(0)
#print(cholera.isna().sum())
cholera.dropna(subset=['total_cases','deaths','case_fatality_rate'],inplace=True)#удаление пустых строк
#cholera.info()
#print(cholera.head(5))

#practice
new_names = ['user_id',
             'total_play_seconds',
             'artist_name',
             'genre_name',
             'track_name'
             ]
#print(new_names)
df.set_axis(new_names,axis='columns',inplace=True)
print(df.isnull().sum())
#print(df.columns)
#print(df.head(10))
#df.info()
shape_table = df.shape
df['track_name']=df['track_name'].fillna('unknown')
df['artist_name']=df['artist_name'].fillna('unknown')
df.dropna(subset=['genre_name'],inplace=True)

print(df.isnull().sum())
print(f'dups: {df.duplicated().sum()}')
df = df.drop_duplicates().reset_index(drop=True)
print(f'dups: {df.duplicated().sum()}')

#shape_table_update = df.shape
#if shape_table == shape_table_update:
#    print(f'Размер таблицы не изменился, текущий размер: {shape_table_update}')
#else:
#    print(f'Таблица уменьшилась, текущий размер: {shape_table_update}')
print(df['genre_name'].unique())
#df['genre_name'] = df['genre_name'].replace('электроника','electronic')
#print(df['genre_name'].unique())
#genre_final_count = df[df['genre_name']=='электроника']['genre_name'].count()
#print(genre_final_count)
print(df.head(10))
print(df.columns)
na_number = df.isna().sum()
print(na_number)
duplicated_number = df.duplicated().sum()
print(duplicated_number)

