from argparse import ArgumentParser
from utility import *

def isEqual(value1, value2):
    """ Check 2 value is equal
        Agrs: Value1 and Value2
        Return: True if 2 value is equal, False otherwise.   
    """
    if (isNaN(value1) and isNaN(value2)): return True
    return (value1 == value2)

def run(args):
    df = readData(args.input)
    data = df.to_dict('list')
    
    removeSamples = []

    for i in range(len(data[list(data.keys())[0]])):
        for j in range(i):
            flag = False
            for key in data:
                if (isEqual(data[key][i], data[key][j]) == False): 
                    flag = True
                    break
            if (flag == False):
                removeSamples.append(i)
                break
    
    print(removeSamples)
    removeSamples.reverse()
    for row in removeSamples:
        for key in data:
            data[key].pop(row)

    writeData(data, args.output)


def main():
    argparser = ArgumentParser()
    argparser.add_argument('-i', '--input', default="./Data/house-prices.csv", help='Input CSV file')
    argparser.add_argument('-o', '--output', default="./Data/result.csv", help='Output CSV file')
    args = argparser.parse_args()

    run(args)
    

if (__name__ == "__main__"):
    main()