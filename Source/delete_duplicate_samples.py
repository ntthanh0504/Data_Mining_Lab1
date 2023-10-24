from argparse import ArgumentParser
import pandas as pd

def isNaN(number):
    """ Check a number is a NaN or not 
        Args: Number
        Return: True if number is NaN, False otherwise
    """

    if (isinstance(number, float) and number != number):
        return True
    return False

def isEqual(value1, value2):
    """ Check 2 value is equal
        Agrs: Value1 and Value2
        Return: True if 2 value is equal, False otherwise.   
    """
    if (isNaN(value1) and isNaN(value2)): return True
    return (value1 == value2)

def run(args):
    df = pd.read_csv(args.input)
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

    df = pd.DataFrame(data)
    df.to_csv(args.output, index = False)


def main():
    argparser = ArgumentParser()
    argparser.add_argument('-in', '--input', default="./Data/house-prices.csv", help='You must be input file path')
    argparser.add_argument('-out', '--output', default="./Data/result.csv", help='You must be input file path')
    args = argparser.parse_args()

    run(args)

if (__name__ == "__main__"):
    main()