from argparse import ArgumentParser
from utility import *


# Extract columns with missing values
def run(args):
    data = readData(args.input)
    data = data.to_dict(orient='list')
    
    features = list(data.keys())
    columns = []
    
    for feature in features:
        for value in data[feature]:
            if isNaN(value):
                columns.append(feature)
                break
    print('Number of columns with missing value : ', len(columns)) 

def main():
    parser = ArgumentParser(description='Impute missing values in a CSV file')
    parser.add_argument('-i', '--input', default="./Data/house-prices.csv", help='You must be input file path')
    parser.add_argument('-o', '--output', default="./Data/result.csv", help='You must be input file path')
    args = parser.parse_args()
    
    run(args)
    
    
if __name__ == "__main__":
    main()
