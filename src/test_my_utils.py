import my_utils as tools
import random as rand

if __name__ == "__main__":

    # First, build the array
    my_array = []
    for i in range(rand.randint(5,20)):
        my_array.append( rand.randint(-1000,1000) )
    print(my_array)

    # Test each function
    print(tools.mean_ints(my_array))
    print(tools.median_ints(my_array))
    print(tools.standard_deviation_ints(my_array))