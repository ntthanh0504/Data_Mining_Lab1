from argparse import ArgumentParser
from utility import *

# Count the number of lines with missing values
def run(args):
    data = readData(args.input)
    data = data.to_dict(orient='list')
    
    features = list(data.keys())
    lines = 0

    for i in range(len(data[features[0]])):
        for feature in features:
            if  isNaN(data[feature][i]):
                lines += 1
                break
    print('Number of lines with missing value: ', lines)

def main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', default="./Data/house-prices.csv", help='Input CSV file')
    parser.add_argument('-o', '--output', default="./Data/result.csv", help='Output CSV file')
    args = parser.parse_args()
    
    run(args)
if __name__ == "__main__":
    main()
    