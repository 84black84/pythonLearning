from pathlib import Path

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
    