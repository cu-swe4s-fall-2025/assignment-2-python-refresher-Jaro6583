#!/bin/bash

echo "Let's test the new dataset:"
python print_fires.py "Albania" -fn "co2_data_subset.csv"
echo ""

echo "Test the 'mean' function:"
python print_fires.py "Albania" -fn "co2_data_subset.csv" -s "mean"
echo ""

echo "Test the 'median' function:"
python print_fires.py "Albania" -fn "co2_data_subset.csv" -s "median"
echo ""

echo "Test the 'standard deviation' function:"
python print_fires.py "Albania" -fn "co2_data_subset.csv" -s "standarddeviation"
echo ""

echo "Now test some errors:"
python print_fires.py "Albania" -fn "co2_data_subset.csv" -s "DoAThing"
python print_fires.py "Albania" -fn "co2_data_subset.csv" -s "Standard Deviation"
python print_fires.py "Albania" -fn "co2_data_subset.csv" -s "StandardError"
echo ""