from pathlib import Path
import pandas as pd
import os

"""
It contains a few helper methods
"""
class HelperClass:
    def getCurrentDirectoryPath(self):
        currentDirectory = ''
        try:
            currentDirectory = Path(__file__).parent.parent
        except:
            currentDirectory = 'C:\CmaCode\python\pythonLearning\PandasFoundamentals'
        return currentDirectory
    
    def getDataFrameFromCsvFile(self, filename):
        mainDirectory = Path(__file__).parent.parent.parent
        filename = filename + '.csv'
        csvPath = os.path.join(mainDirectory, 'Visualization','data', filename)
        df = pd.read_csv(csvPath)
        return df

    