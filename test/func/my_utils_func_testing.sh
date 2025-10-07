test -e ssshtest || curl -q -O https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run FuncTestOfMyUtils python ../../src/my_utils.py mean 8 9 10
assert_in_stdout "Mean: "
assert_in_stdout 9
assert_exit_code 0

run FuncTestOfMyUtils python ../../src/my_utils.py median 21 90 35 50 78
assert_in_stdout "Median: "
assert_in_stdout 50
assert_exit_code 0

run FuncTestOfMyUtils python ../../src/my_utils.py standarddeviation 27 83 41 56
assert_in_stdout "Standard deviation: "
assert_in_stdout 20.75
assert_exit_code 0

run FuncTestOfMyUtils python ../../src/my_utils.py this_function_doesnt_exist 39 73 58
assert_in_stdout "unknown"
assert_exit_code 1