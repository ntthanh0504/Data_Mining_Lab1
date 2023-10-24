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

    for key in data:
        if (isNumeric(data[key]) == False): continue
        values = [value for value in data[key] if (isNaN(value) == False)]
        if (args.method == "z_score"):

            mean = 0
            sd = 0
            if (len(values) != 0):
                mean = sum(values) / len(values)
                sd = (sum([(value - mean) ** 2 for value in values]) / len(values)) **  (1/2)

            for i in range(len(data[key])):
                if (isNaN(data[key][i]) == True or sd == 0): 
                    data[key][i] = 0
                else:
                    data[key][i] = (data[key][i] - mean) / sd

        else:
            min_value = 0
            max_value = 0
            if (len(values) > 0):
                min_value = min(values)
                max_value = max(values)
            
            for i in range(len(data[key])):
                if (isNaN(data[key][i]) == True or (min_value == 0 and max_value == 0)):
                    data[key][i] = 0
                else:
                    data[key][i] = ((data[key][i] - min_value) / (max_value - min_value)) * (args.max - args.min) + args.min
    df = pd.DataFrame(data)
    df.to_csv(args.output, index = False)


def main():
    argparser = ArgumentParser()
    argparser.add_argument('-mtd', '--method', default="min_max", choices=['min_max', 'z_score'], help='You must be input method to normalize')
    argparser.add_argument('-min', '--min', default=0, type=float, help='Input a min value for min_max normalize')
    argparser.add_argument('-max', '--max', default=1, type=float, help='Input a max value for min_max normalize')
    argparser.add_argument('-in', '--input', default="./Data/house-prices.csv", help='You must be input file path')
    argparser.add_argument('-out', '--output', default="./Data/result.csv", help='You must be input file path')
    args = argparser.parse_args()

    run(args)

if (__name__ == "__main__"):
    main()