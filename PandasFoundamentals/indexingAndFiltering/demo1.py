import pandas as pd
import os
from PandasFoundamentals.helperClasses.helperClass import HelperClass

helper = HelperClass()
currentDirectory = helper.getCurrentDirectoryPath()
df = pd.read_pickle(os.path.join(currentDirectory, 'data', 'data_frame.pickle'))
print(currentDirectory)
