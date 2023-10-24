from argparse import ArgumentParser
import pandas as pd

def isNaN(number):
    if (isinstance(number, float) and number != number):
        return True
    return False

def run(args):
    df = pd.read_csv(args.input)
    data = df.to_dict()
    removeColumns = []

    for column in data:
        count = 0
        for index in data[column]:
            if (isNaN(data[column][index])): count += 1
        
        if (count > args.persentage * len(data[column]) / 100):
            removeColumns.append(column)

    for column in removeColumns:
        data.pop(column)

    df = pd.DataFrame(data)
    df.to_csv(args.output, index = False)


def main():
    argparser = ArgumentParser()
    argparser.add_argument('-pst', '--persentage', default=50.0, type=float, help='You must be input persentage')
    argparser.add_argument('-in', '--input', default="./Data/house-prices.csv", help='You must be input file path')
    argparser.add_argument('-out', '--output', default="./Data/result.csv", help='You must be input file path')
    args = argparser.parse_args()

    run(args)

if (__name__ == "__main__"):
    main()