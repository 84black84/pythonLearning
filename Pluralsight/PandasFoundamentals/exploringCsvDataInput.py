# 3. Exploring Pandas Data Input capabilities.py
import pandas as pd
import os

# Where our data lives
currentDirectory = ''
try:
    currentDirectory = os.path.dirname(os.path.realpath(__file__))
except:
    currentDirectory = 'C:\CmaCode\python\pythonLearning\Pluralsight\PandasFoundamentals'

csvPath = os.path.join(currentDirectory, 'data','collection-master','artwork_data.csv')

# All columns that we need
colsToUse = ['id', 'artist',
               'title', 'medium', 'year',
               'acquisitionYear', 'height',
               'width', 'units']

# Read just 5 rows to see what's there
df = pd.read_csv(os.path.join(csvPath), index_col = 'id', usecols = colsToUse)

# Save for later
df.to_pickle(os.path.join(currentDirectory, 'data_pickle', 'data_frame.pickle'))