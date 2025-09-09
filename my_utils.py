def get_column(file_name, query_column, query_value, result_column=1):
    '''
    Searches through a specified data file (designed for csv's) and extracts a subset of a column. Filter by query_value.
    
    Args:
        file_name (str): the name of the file to be looking through
        query_column (int): column you want to check within each row. It should be a 0 if you want to search by area.
        query_value (str): the specific filter you are looking for. So putting a country name here will allow you to filter by country.
        result_column (int, default 1): the data you want from each item through that filter. 3 gives you Forest fires

    Returns:
        A list of the data of interest. The list will be empty if there are no query_value matches found.
    '''
    
    # Build a new array that we will populate to return
    results = []

    # Open file
    try:
        with open(file_name, 'r') as file:
            header = next(file)

            lines = file.read().splitlines()              # "lines" is all the data (the whole file)
            #print("The filetype of 'lines' is: ", type(lines))

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
                        # This except is to catch data values that cannot be converted into ints
                        pass
    
    except FileNotFoundError:
        print("The get_column function cannot find the requested file: " + file_name)

    return results

if __name__ == '__main__':
    print("This is 'main' code! (this shouldn't ever print in this assignment)")