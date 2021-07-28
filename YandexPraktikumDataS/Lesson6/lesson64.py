import pandas as pd
df = pd.read_csv('music_log.csv')
genre_fight = df.loc[:,['genre','Artist']]
genre_pop = genre_fight[genre_fight['genre'] == 'pop']['genre'].count()
genre_rock = genre_fight[genre_fight['genre'] == 'rock']['genre'].count()
print(f'Число прослушанных треков в жанре поп равно {genre_pop}')
print(f'Число прослушанных треков в жанре рок равно {genre_rock}')
if genre_pop > genre_rock:
    print('Попса forever!')
else:
    print('Рок победил!')