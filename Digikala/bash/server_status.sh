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
    IFS=$'\r\n' command eval  'lines=($(cat $input_file))'
    for i in "${!lines[@]}"; do 
        #printf "%s\t%s\n" "$i" "${lines[$i]}"
        flag=Pass
        IFS=$' ' command eval  'elements=(${lines[$i]})'
        for i in "${!elements[@]}"; do
            if [ ${elements[1]} -lt 50 ] ||  [ ${elements[2]} -lt 50 ] ||  [ ${elements[3]} -lt 50 ]; then
                flag=Fail
            fi   
        done
        printf "${elements[0]}: $flag\r\n"
    done
    #printf "${elements[2]}"
else
    echo "input file required!"
fi

