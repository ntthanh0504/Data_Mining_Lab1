from argparse import ArgumentParser
from utility import *

def run(args):
    df = pd.read_csv(args.input)
    data = df.to_dict('list')
    
    removeRows = []

    for i in range(len(data[list(data.keys())[0]])):
        count = 0
        for key in data:
            if (isNaN(data[key][i]) == True): count += 1
        if (count > args.percentage * len(data.keys()) / 100):
            removeRows.append(i)
        
    removeRows.reverse()
    for row in removeRows:
        for key in data:
            data[key].pop(row)

    writeData(data, args.output)
    
def main():
    argparser = ArgumentParser()
    argparser.add_argument('-p', '--percentage', default=50.0, type=float, help='You must be input persentage')
    argparser.add_argument('-i', '--input', default="./Data/house-prices.csv", help='You must be input file path')
    argparser.add_argument('-o', '--output', default="./Data/result.csv", help='You must be input file path')
    args = argparser.parse_args()

    run(args)
    
if (__name__ == "__main__"):
    main()