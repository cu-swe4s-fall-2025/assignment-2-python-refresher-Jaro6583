import argparse
from my_utils import get_column

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

    # Parse the provided arguments
    args = parser.parse_args()
    country = args.area
    country_column = args.country_column
    fires_column = args.fires_column
    file_name = args.file_name

    # Print to make sure we're on track
    #print("So we've got country, country column, fires column, and file name:")
    #print(country, " ", country_column, " ", fires_column, " ", file_name)

    # Finally, execute the actual function
    fires = get_column(file_name, country_column, country, fires_column)
    print(fires)