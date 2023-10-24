from argparse import ArgumentParser
from utility import *

def run(args):
    df = readData(args.input)
    data = df.to_dict('list')
    
    removeColumns = []

    for column in data:
        count = 0
        for value in data[column]:
            if (isNaN(value)): count += 1
        
        if (count > args.percentage * len(data[column]) / 100):
            removeColumns.append(column)

    for column in removeColumns:
        data.pop(column)
    writeData(data, args.output)

def main():
    argparser = ArgumentParser()
    argparser.add_argument('-p', '--percentage', default=50.0, type=float, help='Input percentage')
    argparser.add_argument('-i', '--input', default="./Data/house-prices.csv", help='Input CSV file')
    argparser.add_argument('-o', '--output', default="./Data/result.csv", help='Output CSV file')
    args = argparser.parse_args()
    
    run(args)
    

if (__name__ == "__main__"):
    main()