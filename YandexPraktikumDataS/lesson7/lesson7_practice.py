import pandas as pd
df = pd.read_csv('music_log.csv')
print(df.columns)
df.columns = ['user_id', # заменили названия столбцов
             'total_play_seconds',
             'artist_name',
             'genre_name',
             'track_name'
             ]
print(df.columns)
genre_grouping = df.groupby('user_id')
genre_counting = genre_grouping['genre_name'].count()
print(genre_counting.head(30))



genre_grouping = df.groupby('user_id')['genre_name']


def user_genres(group):
    for col in group:
        if len(col[1]) > 50:
            user = col[0]
            return user
search_id = user_genres(genre_grouping)
print(search_id)