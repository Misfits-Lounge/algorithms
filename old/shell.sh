#!/usr/bin/env bash


#Redhat interview question:
#how to compute the sum of the file size in
#the current directory


#solution:

size=$(ls -ltr | awk '{total+=$5}; END {print total}')

echo $size

