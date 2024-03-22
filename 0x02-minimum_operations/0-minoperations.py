#!/usr/bin/python3
""" module doc"""


    def minOperations(n):
    """" function documetation """
    if n == 1:
        return 0
    operations = float('inf')  # Initialize operations to positive infinity

    # Iterate from 1 to n // 2 (inclusive) to find possible factors
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            operations = min(operations, minOperations(i) + n // i)

    return operations
