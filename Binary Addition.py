"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

"""

import math



def find_next_square(sq):
    s = math.sqrt(sq)
    return (s+1)**2 if (s - math.floor(s) == 0) else None

reslt = find_next_square(625)

print(reslt)