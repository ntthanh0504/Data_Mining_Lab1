import os
import pandas as pd

def isFileExist(filename):
    return os.path.exists(filename)
        
def readData(filename):
    if isFileExist(filename):
        data = pd.read_csv(filename)
        return data
    print('File not found')
    return

def writeData(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"The output CSV file is saved at {filename}.")
    return

def isNaN(value):
    if isinstance(value, float) and value != value:
        return True
    return False

def isNumeric(data, column):
    return all(
        isinstance(value, (int, float)) for value in data[column] if not isNaN(value)
    )

def isCategorical(data, column):
    return all(
        isinstance(value, str) for value in data[column] if not isNaN(value)
    )

