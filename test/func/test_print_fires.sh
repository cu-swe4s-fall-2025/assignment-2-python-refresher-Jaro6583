test -e ssshtest || curl -q -O https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

echo "Let's test the new dataset:"
run print_fires python ../../src/print_fires.py "Albania" -fn "co2_data_subset.csv"
assert_exit_code 0
echo ""

echo "Test the 'mean' function:"
run print_fires python ../../src/print_fires.py "Albania" -fn "co2_data_subset.csv" -s "mean"
assert_exit_code 0
echo ""

echo "Test the 'median' function:"
assert_exit_code 0
echo ""

echo "Test the 'standard deviation' function:"
run print_fires python ../../src/print_fires.py "Albania" -fn "co2_data_subset.csv" -s "standarddeviation"
assert_exit_code 0
echo ""

echo "Now test some errors:"
run print_fires python ../../src/print_fires.py "Albania" -fn "co2_data_subset.csv" -s "DoAThing"
assert_exit_code 1
run print_fires python ../../src/print_fires.py "Albania" -fn "co2_data_subset.csv" -s "Standard Deviation"
assert_exit_code 1
run print_fires python ../../src/print_fires.py "Albania" -fn "co2_data_subset.csv" -s "StandardError"
assert_exit_code 1
echo ""