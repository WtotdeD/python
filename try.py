

from pathlib import Path
print("File      Path:", Path(__file__).absolute())
print("Directory Path:", Path().absolute())  


import pandas as pd

df = pd.read_csv(r"data//XLS200702165807.csv", na_values= ['no info', '.'])

print(df.head(5))

print(df['Muntsoort'].dtypes)

print(df['Rekeningnummer'][2])


print(df.shape)

print(df.columns)


