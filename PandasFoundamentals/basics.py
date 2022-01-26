import pandas as pd
import os
from helperClasses.helperClass import HelperClass 

helper = HelperClass()
currentDirectory = helper.getCurrentDirectoryPath()
# df = pd.read_pickle(os.path.join(currentDirectory, 'data_pickle', 'data_frame.pickle'))
print(currentDirectory)