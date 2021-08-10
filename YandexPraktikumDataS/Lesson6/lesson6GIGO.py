import pandas as pd
df = pd.read_csv('music_log.csv')
#Теория
measurements = [['Солнце',146,152], # Измерения хранятся в списке списков
              ['Луна',0.36, 0.41], # measurements (англ. measurement, «измерение»).
              ['Меркурий',82, 217],
              ['Венера',38, 261],
              ['Марс',56,401],
              ['Юпитер',588, 968],
              ['Сатурн',1195, 1660],
              ['Уран',2750, 3150],
              ['Нептун', 4300, 4700],
              ['Комета Галлея', 6, 5400]]
# Названия столбцов хранятся в переменной header.
header = ['Небесные тела ','MIN', 'MAX']
# Сохраним структуру данных в переменной celestial (англ. celestial, «небесный»).
celestials = pd.DataFrame(data=measurements,columns=header)
#print(celestials.columns)
celestials.set_axis(['celestial_bodies','min_distance','max_distance'], axis='columns', inplace=True)
#print(celestials)

#Практика
#print(df.columns)
new_names = ['user_id',
             'total_play_seconds',
             'artist_name',
             'genre_name',
             'track_name'
             ]
#print(new_names)
df.set_axis(new_names,axis='columns',inplace=True)

print(df.columns)
print(df.head(10))