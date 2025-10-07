import argparse
import my_utils
import sys

if __name__ == '__main__':

    # Builder parser object
    parser = argparse.ArgumentParser(description="Search for the amount of "
                                     + "CO2 emissions caused by wildfires in "
                                     + "a certain area/region")

    # Now add expected arguments
    # 1) Country/area
    parser.add_argument("area", type=str, help="The area to look for the data"
                        + " of interest (default interest: fires)")
    parser.add_argument("-cc", "--country-column", type=int, default=0,
                        help="This is the column that will be looked through "
                        + "to find a match for Area. You can switch this "
                        + "column to 1 if you want to search by year, for "
                        + "example.")
    parser.add_argument("-fc", "--fires-column", type=int, default=3,
                        help="This is the column that contains the fire data."
                        + " You can select a different column to extract "
                        + "different data.")
    parser.add_argument("-fn", "--file-name", type=str,
                        default="Agrofood_co2_emission.csv",
                        help="This is the name of the file that will be "
                        + "looked through")
    parser.add_argument("-s", "--statistic", type=str, default="no_statistic",
                        help=f"Allows the user to specify what statstic "
                        + "should be performed on the extracted dataset. "
                        + "Type 'mean', 'median', or 'standarddeviation'.")

    # Parse the provided arguments
    args = parser.parse_args()
    country = args.area
    country_column = args.country_column
    fires_column = args.fires_column
    file_name = args.file_name
    statistic = args.statistic

    # Execute the extraction function
    fires = my_utils.get_column(file_name, country_column,
                                country, fires_column)

    # Lowercase the requested statistic
    statistic = statistic.lower()

    # Perform any requested statistic
    if statistic == 'no_statistic':
        print(fires)
    elif statistic == "mean":
        print(my_utils.mean_ints(fires))
    elif statistic == "median":
        print(my_utils.median_ints(fires))
    elif statistic == "standarddeviation":
        print(my_utils.standard_deviation_ints(fires))
    else:
        print("An unknown statistic has been requested")
        sys.exit(1)
