import pandas as pd
import os


# Initialize Data structures
df1 = pd.read_csv('source.csv')
df2 = pd.read_csv('addresses.csv')

df1 = df1.reset_index()  # make sure indexes pair with number of rows
df2 = df2.reset_index()

for index, row in df1.iterrows():
    if index % 1000 == 0:
        print('reached row:', index)
    for index2, row2 in df2.iterrows():
        if row[1].lower() == row2[1].lower():
            print('match', row[1], row2[1])

print('No more matches')


