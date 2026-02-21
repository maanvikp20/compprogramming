# get first 499k squares and find odds

1 , 4, 9, 16, 25, 36

squares = [x**2 for x in range(1, 499001)]
sumOdds = sum([x for x in squares if x % 2 != 0])
print(sumOdds)