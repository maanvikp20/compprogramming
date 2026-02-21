# 5 kyu - Weight for weight

input = " 40 103 123 4444 99 2000"

def order_weight(strng):
    strng = strng.split()
    strng.sort(key=lambda x: (sum(int(digit) for digit in x), x))
    return " ".join(strng)

print(order_weight(input))