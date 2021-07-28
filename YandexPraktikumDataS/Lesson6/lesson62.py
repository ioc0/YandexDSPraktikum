import pandas as pd
df = pd.read_csv('music_log.csv')

observations_info_table = df.shape[0]
observations_table = 67963

if observations_info_table == observations_table:
    print('Решение верно, количество наблюдений равно', observations_table)
else:
    print('Решение неверно, проверьте ещё раз!')
