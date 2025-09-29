test -e ssshtest || curl -q -O https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_my_utils python ../../src/test_my_utils.py
assert_in_stdout "Mean: "
assert_exit_code 0