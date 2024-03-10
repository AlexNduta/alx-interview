#!/usr/bin/python3
""" -Create a Pacal triangle
     [1]
    [1,1]
    [1,2,1]
    []
"""


def pascal_triangle(n):
    """
    - The function should take an interger that represts the size
    of the array
    - we should  firt chaeck if the interger passed is greater than 0
    which means that the array is invalid
    - We then loop through the array
    - In every loop, we create a temporary loop which is the array
    being looped though but with zeros amended on both ends
    - Also create an empty arrsy that will represent what
    to return eventualy
   - We then loop though the temporary array
   - we add the first two adjacent digits will will
   give us the value of the item above it

    """
    result = [[1]]
    if n <= 0:
        return []
    else:
        # iterate through the array continously
        for i in range(n - 1):
            temp = [0] + result[-1]+[0]
            row = []
            for j in range(len(temp)-1):
                row.append(temp[j] + temp[j + 1])
            result.append(row)
        return result
