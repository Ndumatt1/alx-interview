#!/usr/bin/python3
''' UTF-8 Validation '''


def validUTF8(data):
    ''' Determines if a given data set represents a valid UTF-8 encoding '''
    num_of_bytes = 1

    for byte in data:
        if num_of_bytes == 1:
            if byte >> 5 in [6, 5]:
                num_of_bytes = 2
            elif byte >> 4 == 14:
                num_of_bytes = 3
            elif byte >> 3 == 30:
                num_of_bytes = 4
            elif byte >> 7 == 1:
                return False

        else:
            if byte >> 6 != 2:
                return False
            num_of_bytes -= 1
    return num_of_bytes == 1
