# 5 kyu - Perimeter of squares in a rectangle

def perimeter(n):
    a, b = 0, 1
    sum = 0
    for i in range(0, n+1):
        a, b = b, a+b
        sum += a
    return sum * 4

print(perimeter(100))