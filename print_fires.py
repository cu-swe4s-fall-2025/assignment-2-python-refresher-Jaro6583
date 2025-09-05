from my_utils import get_column

country='United States of America'
county_column = 0           # This was originally set to 1, which I think is a mistake
fires_column = 3            # This was originally set to 4, which I think is a mistake
file_name = 'Agrofood_co2_emission.csv'
fires = get_column(file_name, county_column, country, fires_column)
print(fires)
