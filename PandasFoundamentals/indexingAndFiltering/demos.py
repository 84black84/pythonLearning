import pandas as pd
import os
from PandasFoundamentals.helperClasses.helperClass import HelperClass

helper = HelperClass()
currentDirectory = helper.getCurrentDirectoryPath()
df = pd.read_pickle(os.path.join(currentDirectory, 'data', 'data_frame.pickle'))

# Demo1
artists = df['artist']
pd.unique(artists)

# Demo2
francis = df['artist'] == 'Bacon, Francis'
francis.value_counts()

# Demo3
df.loc[1035, 'artist']
df.iloc[0, 0]
df.iloc[0, :]
df.iloc[0:2,0:2]

# Try multiplication
df['height'] * df['width']

# Try to convert
pd.to_numeric(df['width'])

# Force NaNs
pd.to_numeric(df['width'], errors='coerce')
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')

pd.to_numeric(df['height'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')

# Try multiplication after cleaning
df['height'] * df['width']
df['units'].value_counts()

# Assign - create new columns with size
area = df['height'] * df['width']
df = df.assign(area = area)

df['area'].max()
df['area'].idxmax()
df.loc[df['area'].idxmax(), :]