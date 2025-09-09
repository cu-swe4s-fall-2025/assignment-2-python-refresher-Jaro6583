#!/bin/bash

echo "First, let's look at fires in the USA:"
python print_fires.py "United States of America"
echo "Hey, that worked!"
echo ""

echo "Next, let's force an error by trying to read a datasheet that doesn't exist:"
python print_fires.py "Albania" -fn "DoesntExist.csv"
echo ""

echo "Lastly, let's force another error by forgetting to specify which area we are interested in:"
python print_fires.py