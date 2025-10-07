[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

The my_utils.py file contains the get_column function. That function reads in a data file (preferably a csv), then parses it as specified by the user.
The print_fires.py file is designed to be executed from a command line. Argparse has been used to make the inputs easy to control. Execute "python print_fires.py -h" to pull up the argparse help page for that file.
The run.sh file calls the print_fires.py file three times. The first time, it gathers the forest fire data from the USA. The next two times, it tries to call the print_fires.py file but makes mistakes.

Assignment 4 update:
I've added mean, median, and standard deviation calculating functions into the my_utils.py file. I've also created a new file, test_my_utils.py, that tests each of these functions using arrays of random size and values. To the print_fires.py file, I added an additional optional argument where the user can specify a statistic (one of the three I just added) to apply to the dataset of interest. I created the test_print_fires.sh file to test this new argument. I also created a new csv file called co2_data_subset.csv which is literally just a subset of the whole data found in Agrofood_co2_emission.csv. The test_print_fires.sh file calls this new subset rather than the original.

Assignment 5 update:
I've added two YAML files. One (in the root) serves as the environment file for all my stuff. The other (in .github/workflows/testing.yml) is for the GitHub actions control. I have it so that on all pushes and for pull requests to the master branch it runs the tests. I have two unit test files (both .py) and two functional test files (both .sh). I also have a linter which was a pain to satisfy. Should all be good to go now.