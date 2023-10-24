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

def isNumeric(values):
    for value in values:
        if (isNaN(value)): continue
        if (type(value) != int and type(value) != float): return False
    
    return True

def run(args):
    df = pd.read_csv(args.input)
    data = df.to_dict('list')

    if (isNumeric(data[args.attribute1]) == False or isNumeric(data[args.attribute2]) == False):
        raise Exception("Attribute is not a numeric")
    
    values1 = [value if isNaN(value) == False else 0 for value in data[args.attribute1]]
    values2 = [value if isNaN(value) == False else 0 for value in data[args.attribute2]]

    values = []
    if (args.operator == 'addition'):
        values = [values1[i] + values2[i] for i in range(len(values1))]
    elif (args.operator == 'subtraction'):
        values = [values1[i] - values2[i] for i in range(len(values1))]
    elif (args.operator == 'multiplication'):
        values = [values1[i] * values2[i] for i in range(len(values1))]
    else:
        values = [values1[i] / values2[i] if (values2[i] != 0) else 0 for i in range(len(values1))]
    data[args.key] = values

    df = pd.DataFrame(data)
    df.to_csv(args.output, index = False)

def main():
    argparser = ArgumentParser()
    argparser.add_argument('attribute1', help='You must be input attribute to performing')
    argparser.add_argument('attribute2', help='You must be input attribute to performing')
    argparser.add_argument('-opt', '--operator', default="addition", choices=['addition', 'subtraction', 'multiplication', 'division'], help='You must be input operator to performing')
    argparser.add_argument('-k', '--key', default='result', help='input key to store result')
    argparser.add_argument('-in', '--input', default="./Data/house-prices.csv", help='You must be input file data path')
    argparser.add_argument('-out', '--output', default="./Data/result.csv", help='You must be input file ouput path')
    args = argparser.parse_args()

    run(args)

if (__name__ == "__main__"):
    main()