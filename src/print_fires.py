import argparse
import my_utils
import sys

if __name__ == '__main__':

    # Builder parser object
    parser = argparse.ArgumentParser(description="Search for the amount of CO2 emissions caused by wildfires in a certain area/region")

    # Now add expected arguments
    # 1) Country/area
    parser.add_argument("area", type=str, help="The area to look for the data of interest (default interest: fires)")

    # 2) Country column argument
    # This selects the column that the function will sift through looking for matches to the Area string
    parser.add_argument("-cc", "--country-column", type=int, default=0, help="This is the column that will be looked through to find a match for Area. You can switch this column to 1 if you want to search by year, for example.")

    # 3) Fires column argument
    # This selects the column that has the data of interest 
    parser.add_argument("-fc", "--fires-column", type=int, default=3, help="This is the column that contains the fire data. You can select a different column to extract different data.")

    # 4) File name argument
    # This selects the name of the argument
    parser.add_argument("-fn", "--file-name", type=str, default="Agrofood_co2_emission.csv", help="This is the name of the file that will be looked through")

    #5) Statistical function argument
    # This allows the user to specify what statistics they would like to apply to the extracted dataset.
    parser.add_argument("-s", "--statistic", type=str, default="no_statistic", help="Allows the user to specify what statstic should be performed on the extracted dataset. Type 'mean', 'median', or 'standarddeviation'.")

    # Parse the provided arguments
    args = parser.parse_args()
    country = args.area
    country_column = args.country_column
    fires_column = args.fires_column
    file_name = args.file_name
    statistic = args.statistic

    # Print to make sure we're on track
    #print("So we've got country, country column, fires column, and file name:")
    #print(country, " ", country_column, " ", fires_column, " ", file_name)

    # Execute the extraction function
    fires = my_utils.get_column(file_name, country_column, country, fires_column)

    # Perform any requested statistic
    if statistic == 'no_statistic':
        print(fires)
    elif statistic == "mean" or statistic == "Mean":
        print(my_utils.mean_ints(fires))
    elif statistic == "median" or statistic == "Median":
        print(my_utils.median_ints(fires))
    elif statistic == "standarddeviation" or statistic == "Standarddeviation" or statistic == "StandardDeviation":
        print(my_utils.standard_deviation_ints(fires))
    else:
        print("An unknown statistic has been requested")
        sys.exit(1)