#!/usr/bin/python3
''' calculates the minimum operation needed to result in n H chars '''


def minOperations(n):
    '''
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file
    '''
    if n <= 0:
        return 0
    min_operations = 0
    clipboard = 0
    file_content = 1

    while file_content < n:
        if n % file_content == 0:
            clipboard = file_content
            min_operations += 1
        file_content += clipboard
        min_operations += 1
    return min_operations
