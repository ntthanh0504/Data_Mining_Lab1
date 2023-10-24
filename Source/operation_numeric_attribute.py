from argparse import ArgumentParser
from utility import *

def run(args):
    df = readData(args.input)
    data = df.to_dict('list')

    if not isNumeric(data, args.attribute1) or not isNumeric(data, args.attribute2):
        raise Exception("Attribute is not a numeric")
    
    values1 = [value if not isNaN(value) else 0 for value in data[args.attribute1]]
    values2 = [value if not isNaN(value) else 0 for value in data[args.attribute2]]

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

    writeData(data, args.output)

def main():
    parser = ArgumentParser()
    parser.add_argument("attribute1", help="The first attribute to perform the operation on.")
    parser.add_argument("attribute2", help="The second attribute to perform the operation on.")
    parser.add_argument("-opt", "--operator", default="addition", 
                        choices=["addition", "subtraction", "multiplication", "division"], 
                        help="The mathematical operation to perform.",
    )
    parser.add_argument("-k", "--key", default="result", help="The name of the new column to store the result in.")
    parser.add_argument("-i", "--input", default="./Data/house-prices.csv", help="The path to the input CSV file.")
    parser.add_argument("-o", "--output", default="./Data/result.csv", help="The path to the output CSV file.")
    args = parser.parse_args()

    run(args)

if (__name__ == "__main__"):
    main()