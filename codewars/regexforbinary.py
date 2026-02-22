# 4 kyu - Regular Expressions for Binary Numbers divisible by 5
# come back

import re

def binary_divisible_by_5():
    pattern = r'0|(101(0)*)$'
    return re.compile(pattern)

print(binary_divisible_by_5().match("10000111"))