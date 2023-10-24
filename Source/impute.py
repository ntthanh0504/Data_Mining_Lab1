from argparse import ArgumentParser
from utility import *

# Fill in the missing values with the mean, median (for numeric properties) 
# and mode (for the categorical attribute)
def fill_na(data, column, replace_value):
    for i, current_value in enumerate(data[column]):
        if isNaN(current_value):
            data[column][i] = replace_value
    return pd.DataFrame(data)

def mean(data, column):
    non_missing_data = [value for value in data[column] if not isNaN(value)]
    mean = sum(non_missing_data)/len(non_missing_data)
    return round(mean)

def median(data, column):
    non_missing_data = [value for value in data[column] if not isNaN(value)]
    # Sort the data.
    non_missing_data.sort()

    # Calculate the median.
    n = len(non_missing_data)
    if n % 2 == 0:
        median = (non_missing_data[n // 2] + non_missing_data[n // 2 - 1]) / 2
    else:
        median = non_missing_data[n // 2]

    return median

def mode(data, column):
    non_missing_data = [value for value in data[column] if not isNaN(value)]
    # Create a dictionary to store the frequency of each value.
    get_mode = {}
    for value in non_missing_data:
        if value in get_mode:
            get_mode[value] += 1
        else:
            get_mode[value] = 1

    # Get the maximum frequency.
    max_value = max(get_mode.values())

    # Get the values with the maximum frequency.
    mode_values = [
        key for key, value in get_mode.items() if value == max_value
    ]
    
    return mode_values[0]
            
def run(args):
    data = readData(args.input)
    data = data.to_dict(orient='list')
    
    # check column is numeric or categorical column 
    if args.method not in ["mean", "median", "mode"]:
        print("Method is not supported.")
        return None

    for column in args.columns.split():
        if isNumeric(data, column):
            if args.method == "mean":
                mean_value = mean(data, column)
                data = fill_na(data, column, mean_value)
            
            elif args.method == 'median':
                median_value =median(data, column)
                data = fill_na(data, column, median_value)
            
            else:
                print(f'Method is not supported for numeric column - {column}')
        
        elif isCategorical(data, column):
            if args.method == 'mode':
                mode_value = mode(data, column)
                data = fill_na(data, column, mode_value)
            else:
                print(f'Method is not supported for categorical column - {column}')
        else:
            print(f'Column - {column} is not numeric or categorical')

    writeData(data, args.output)

def main():
    parser = ArgumentParser(description='Impute missing values in a CSV file')
    parser.add_argument('-i', '--input', default="./Data/house-prices.csv", help='Input CSV file')
    parser.add_argument('-o', '--output', default="./Data/result.csv", help='Output CSV file')
    parser.add_argument('--method', default="mode", help='Imputation method')
    parser.add_argument('--columns', default="LotFrontage Alley", help='Columns to impute')
    args = parser.parse_args()
    
    run(args)
        
     
if __name__ == "__main__":
    main()
