import pandas as pd
import os
from PandasFoundamentals.helperClasses.helperClass import HelperClass

helper = HelperClass()
currentDirectory = helper.getCurrentDirectoryPath()
df = pd.read_pickle(os.path.join(currentDirectory, 'data', 'data_frame.pickle'))

# Simplest default plot
acquisition_years = df.groupby('acquisitionYear').size()
acquisition_years.plot()