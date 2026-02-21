fibonacciTerms = [1, 2]
while fibonacciTerms[-1] < 4000000:
  fibonacciTerms.append(fibonacciTerms[-1] + fibonacciTerms[-2])

evenTermSum = sum([x for x in fibonacciTerms if x % 2 == 0])
print(evenTermSum)
# 4613732