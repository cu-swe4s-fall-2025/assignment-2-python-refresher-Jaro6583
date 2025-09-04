def get_column(file_name, query_column, query_value, result_column):
    '''
    file_name is just the name of the file to be looking through
    query_column is the column you want to check (this should be an integer) within each row. It should be a 0 if you want to search by area.
    query_value is the specific filter you are looking for. So putting a country name here will allow you to filter by country. This should (probably) be a string.
    result_column is the data you want from each item through that filter. It should be an integer. 3 gives you Forest fires
    '''
    
    # Build a new array that we will populate to return
    results = []

    # Open file
    with open(file_name, 'r') as file:
        header = next(file)

        lines = file.read().splitlines()              # "lines" is all the data. The whole file
        #print("The filetype of 'lines' is: ", type(lines))

        # Now go through and make an array out of each row
        for line in range(len(lines)):
            row = lines[line].strip().split(',')
            #print(column)

            # Check to see if query_column matches query_value
            if row[query_column] == query_value:
                results.append(row[result_column])
    
    return results
