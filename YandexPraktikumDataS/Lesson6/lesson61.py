
import pandas as pd

# <напишите код здесь>
music = [['Metallica','Sandman'],
         ['Poets of fall','feed the rain'],
         ['Prodigy','smack my bitch'],
         ['Pendulum','Sugar'],
         ['Quesmist','Warrior Song']
        ]
entries = ['artist','track']

playlist = pd.DataFrame(data=music,columns=entries)

print(playlist)