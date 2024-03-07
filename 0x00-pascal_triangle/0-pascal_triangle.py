#!/usr/bin/python3
""" 
    -Create a Pacal triangle
     [1]
    [1,1]
    [1,2,1]
    []
"""
def pascal_triangle(n):
    result=[[1]]
    if n <= 0:
        return []
    else:
        # iterate through the array continously
        for i in range(n -1):
            temp = [0] + result[-1]+[0]
            row = []
            for j in range(len(temp)-1):
                row.append(temp[j] + temp[j +1])
            result.append(row)
        return result

