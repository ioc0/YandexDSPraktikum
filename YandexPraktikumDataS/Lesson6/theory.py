import pandas as pd

atlas = [
    ['Франция', 'Париж'],
    ['Россия', 'Москва'],
    ['Китай', 'Пекин'],
    ['Мексика', 'Мехико'],
    ['Египет', 'Каир']
]
table_head = ['Country','Capital']

world_map = pd.DataFrame(data=atlas,columns=table_head)
#print(world_map)

df = pd.read_csv('music_log.csv')
#print(df.info())
'''
print(df.head(10))
print(df.tail(10))
new_df = df.sort_values(['total play'])
print('--'*32)
print(new_df)
print(df.dtypes)

#print(df.loc[1:15,['genre','total play']])
data = [[0,0,0,0,0,0,0,0,0,0],
        [0,'-','-','-',0,0,0,0,0,0],
        [0,'-','X','-',0,0,'X','X','X','X'],
        [0,'-','X','-',0,0,0,0,0,0],
        [0,'-','-','-',0,0,0,0,0,0],
        [0,0,'-',0,0,0,0,0,'X',0],
        [0,'-','X','X',0,0,0,0,0,0],
        [0,0,'-','-',0,0,0,0,0,0],
        [0,0,0,0,'-','X',0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
columns = ['A','B','C','D','E','F','G','H','I','J']
battle = pd.DataFrame(data = data, columns = columns)
print(battle)
print(battle.loc[:,['B']])
print(battle.loc[5:7])
print(battle.loc[:,'A':'E'])
print(battle.loc[:,'F':'J'])

//теория выборка
ВИД	                                    РЕАЛИЗАЦИЯ	                                                СОКРАЩЁННАЯ ЗАПИСЬ
Все строки, удовлетворяющие условию	    battle.loc[battle.loc[:,'В'] == 'X']	                    battle[battle['В'] == 'X']
Столбец, удовлетворяющий условию	    battle.loc[battle.loc[:,'В'] == 'X']['В']	                battle[battle['В'] == 'X']['В']
Применение метода	                    battle.loc[battle.loc[:,'В'] == 'X']['В'].count()	        battle[battle['В'] == 'X']['В'].count()
'''
total_play = df.loc[:,'total play']
#print(total_play.loc[total_play <= 10])

#Практика
rock = df.loc[df.loc[:,'genre'] == 'rock']
rock_time = rock['total play']
rock_haters = rock_time.loc[rock_time.loc[:] <= 5].count()
#print(f'Количество пропущенных треков жанра рок равно {rock_haters}')
pop = df.loc[df.loc[:,'genre'] == 'pop']
pop_time = pop['total play']
pop_haters = pop_time.loc[pop_time.loc[:] <=5].count()
#print(f'Количество пропущенных треков жанра поп равно {pop_haters}')
rock_skip = rock_haters/rock.shape[0]
pop_skip = pop_haters/pop.shape[0]
print('Доля пропущенных композиций жанра рок равна: {:.5f}'.format(rock_skip))
print('Доля пропущенных композиций жанра поп равна: {:.5f}'.format(pop_skip))