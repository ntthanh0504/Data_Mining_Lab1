from argparse import ArgumentParser
from utility import *
    
def run(args):
    df = readData(args.input)
    data = df.to_dict(orient='list')

    for column in data:
        if not isNumeric(data, column):
            continue
        values = [value for value in data[column] if not isNaN(value)]

        if args.method == 'z_score':
            data = normalize_using_z_score(data, column, values)
        elif args.method == 'min_max':
            data = normalize_using_min_max(data, column, values, args.min, args.max)
        else:
            raise ValueError('Invalid normalization method: {}'.format(args.method))

    writeData(data, args.output)


def normalize_using_z_score(data, column, values):
    mean, sd = 0, 0
    if len(values) != 0:
        mean = sum(values) / len(values)
        sd = (sum([(value - mean) ** 2 for value in values]) / len(values)) ** 0.5

    for i in range(len(data[column])):
        if isNaN(data[column][i]) or sd == 0:
            data[column][i] = 0
        else:
            data[column][i] = (data[column][i] - mean) / sd
            
    return data


def normalize_using_min_max(data, column, values, min_value_scaling, max_value_scaling):

    min_value, max_value = 0, 0
    if (len(values) > 0):
        min_value = min(values)
        max_value = max(values)

    for i in range(len(data[column])):
        if isNaN(data[column][i]) or min_value == max_value:
            data[column][i] = 0
        else:
            data[column][i] = ((data[column][i] - min_value) / (max_value - min_value)) * (max_value_scaling - min_value_scaling) + min_value_scaling
    return data

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--method', default='min_max', choices=['min_max', 'z_score'], help='Input method for normalize')
    parser.add_argument('--min', default=0, type=float, help='Input a min value for min_max normalize')
    parser.add_argument('--max', default=1, type=float, help='Input a max value for min_max normalize')
    parser.add_argument('--input', default='./Data/house-prices.csv', help='You must be input file path')
    parser.add_argument('--output', default='./Data/result.csv', help='You must be input file path')
    args = parser.parse_args()

    run(args)