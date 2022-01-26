# 3. Exploring Pandas Data Input capabilities.py
import pandas as pd
import os
from PandasFoundamentals.helperClasses.helperClass import HelperClass

# Where our data lives
helper = HelperClass()
currentDirectory = helper.getCurrentDirectoryPath()
csvPath = os.path.join(currentDirectory, 'data','collection-master','artwork_data.csv')

# All columns that we need
colsToUse = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']

# Proper data loading
df = pd.read_csv(csvPath, usecols=colsToUse, index_col='id')

# Save for later
df.to_pickle(os.path.join(currentDirectory, 'data', 'data_frame.pickle'))