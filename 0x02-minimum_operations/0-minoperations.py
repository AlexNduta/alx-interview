#!/usr/bin/env python3

def minOperations(n):
    operations = 0 # number of operations to carry out
    current_Length = 1 # length of the element, initially 1
    # loop through till the length is 0
    while current_Length < n:
        # if the value of n is a multiple of add onne to operations
        if n % current_Length == 0:
            operations = operations + 1 #  copyAll
            current_Length = current_Length * 2 # paste operation
        else:
            operations = operations + 2
            current_Length = current_Length + current_Length
    return operations
