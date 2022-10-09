#!/bin/bash

# NOTE:
# * Your script MUST read the input from a given file as follows:
#   $ ./count_names.sh input.txt
# * Your script MUST print the result to the stdout.
# * Your script MUST conform to the output format provided in the question.
#
# ATTENTION: DON'T change this file name!

if [ -f "$1" ]; then
    input_file=$1
    # echo $input_file
    # awk 'BEGIN{c=0} //{c++} END{print "Count: ",c}' RS="[[:space:]]" $input_file
    count=$(cat $input_file | tr ',' ' ' | tr '|' ' ' | tr '$' ' ' | tr '!' ' ' | tr '  ' ' ' | tr '\\' ' ' | tr '\n' ' ' |  wc -w)
    printf "Count: $count"
else
    echo "input file required!"
fi
