import pandas as pd
exo = pd.read_csv('exoplanet.eu_catalog.csv')


#print(f'empty spaces: {exo.isna().sum()}')
#print(f'duplicates: {exo.duplicated().sum()}')
#print(exo.columns)
#exo.columns = ['#','name','property','mass','radius','discovered']
#print(exo.head(5))

exo.dropna()
exo.info()

radius = exo['radius']
print(radius.sort_values(ascending=False).head(30))
print(exo[exo['radius']<1])

exo_small = exo[(exo['radius']<1)&(exo['discovered']==2014)] # поиск с двумя условиями
print(exo_small)

#print(exo['radius'].sort_values(by='radius',ascending=True).head(30))