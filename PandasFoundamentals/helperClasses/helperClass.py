from pathlib import Path

"""
It contains a few helper methods
"""
class HelperClass:
    def getCurrentDirectoryPath(self):
        currentDirectory = ''
        currentDirectory = Path(__file__).parent.parent
        return currentDirectory
    