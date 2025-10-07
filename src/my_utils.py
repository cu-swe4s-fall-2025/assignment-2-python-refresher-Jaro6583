def get_column(file_name, query_column, query_value, result_column=1):
    '''
    Searches through a specified data file (designed for csv's) and extracts
    a subset of a column. Filter by query_value.

    Args:
        file_name (str): the name of the file to be looking through
        query_column (int): column you want to check within each row.
            It should be a 0 if you want to search by area.
        query_value (str): the specific filter you are looking for.
            Putting a country name here will allow you to filter by country.
        result_column (int, default 1): the data you want from each item
            through that filter. 3 gives you Forest fires

    Returns:
        A list of the data of interest. The list will be empty if
        there are no query_value matches found.
    '''
    
    # Build a new array that we will populate to return
    results = []

    # Open file
    try:
        with open(file_name, 'r') as file:
            header = next(file)
            lines = file.read().splitlines()
            
            # Now go through and make an array out of each row
            for line in range(len(lines)):
                row = lines[line].strip().split(',')
                #print(column)

                # Check to see if query_column matches query_value
                if row[query_column] == query_value:
                    try:
                        datapoint = int(float(row[result_column]))
                        results.append(datapoint)
                    except ValueError:
                        '''
                        This except is to catch data values that cannot be
                        converted into ints
                        '''
                        pass
    
    except FileNotFoundError:
        print(
            f"The get_column function cannot find the requested file: "
            + file_name
            )

    return results

def mean_ints(array_of_ints=[]):
    '''
    This function is meant to read an array of integers and return the average
    (mean) of those integers.
    If no array is given, the default will be an empty array (the first "if"
    check is to look for this case).
    This function will also convert the integers into floats in order for the
    math to work.
    Returns a float
    '''
    
    if len(array_of_ints) == 0:
        print("No array submitted. Mean cannot be calculated.")
    else:
        sum = 0.0
        for i in range(len(array_of_ints)):
            try:
                sum += float(array_of_ints[i])
            except ValueError:
                print(
                    f"Submitted array contains values that cannot "
                    + "be converted to integers."
                    )
        mean = sum/len(array_of_ints)

        # For convenience, let's round to the nearest hundredth
        mean = round(mean * 100)/100
        
        return mean
    
def median_ints(array_of_ints=[]):
    '''
    This function will read an array of integers and return the median value.
    If there is an even number of entries in the array, the function will
    average the middle two values.
    This function will also convert the integers into floats.
    Returns a float
    '''
    if len(array_of_ints) == 0:
        print("No array submitted. Median cannot be calculated.")
        median = "MedianError"
    else:
        try:
            # First, reorder the array to put it in order
            array_of_ints.sort()
            
            if len(array_of_ints) % 2 == 1:
                # This is an odd number of entries
                median = float(array_of_ints[ int((len(array_of_ints) - 1) / 2) ])
            else:
                # This is an even number of entries
                median = float(
                    (array_of_ints[ int(len(array_of_ints) / 2 - 1) ])
                    + float(array_of_ints[ int(len(array_of_ints) / 2) ]))
                median /= 2.0
        except ValueError:
            print("Submitted array contains values that cannot be used to "
                  + "find a median.")
    
    return median

def standard_deviation_ints(array_of_ints=[]):
    '''
    This function will read an array of integers and return the standard
    deviation.
    This function will also convert the integers into floats in order for the
    math to work.
    Returns a float
    '''

    if len(array_of_ints) == 0:
        print("No array submitted. Standard deviation cannot be calculated.")
        standard_deviation = "SD_Error"
    else:
        standard_deviation = 0
        mean = mean_ints(array_of_ints)
        for i in range(len(array_of_ints)):
            standard_deviation += (array_of_ints[i] - mean)**2
        
        standard_deviation /= len(array_of_ints)
        standard_deviation = standard_deviation**(1/2)

        # For convenience, let's round to the nearest hundredth's place
        standard_deviation = round(standard_deviation * 100)/100
    
    return standard_deviation

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description=f"Directly calling this function and providing numbers "
            + "will provide the requested statistic from those numbers.")
    parser.add_argument("function", type=str, default="mean", help=f"The "
                        + "function requested. Type 'mean', 'median', or "
                        + "'standarddeviation'.")
    parser.add_argument("numbers", type=float, nargs='+', help="A list of "
                        + "numbers for the requested function to be "
                        + "applied to.")

    args = parser.parse_args()

    if args.function == "mean":
        mean = mean_ints(args.numbers)
        print(f"Mean: {mean}")
    elif args.function == "median":
        median = median_ints(args.numbers)
        print(f"Median: {median}")
    elif args.function == "standarddeviation":
        SD = standard_deviation_ints(args.numbers)
        print(f"Standard deviation: {SD}")
    else:
        print("An unknown statistic has been requested")
        sys.exit(1)