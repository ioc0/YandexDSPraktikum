import pandas as pd
df = pd.read_csv('music_log.csv')
slice_1 = df.loc[:,['genre','total play','track']]
rock = slice_1[slice_1['genre']=='rock']['genre']
print(rock)


