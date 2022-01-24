# 3. Exploring Pandas Data Input capabilities.py

import pandas as pd
import os

# Where our data lives
CSV_PATH = os.path.join('Pluralsight', 'PandasFoundamentals', 'data', 'collection-master', 'artwork_data.csv')

# All columns that we need
colsToUse = ['id', 'artist',
               'title', 'medium', 'year',
               'acquisitionYear', 'height',
               'width', 'units']

# Read just 5 rows to see what's there
df = pd.read_csv('C:\CmaCode\python\pythonLearning\Pluralsight\PandasFoundamentals\data\collection-master\\artwork_data.csv',
                 index_col = 'id', 
                 usecols = colsToUse)

# Save for later
df.to_pickle(os.path.join('..', 'data_frame.pickle'))