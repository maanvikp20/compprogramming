testnum = 600851475143
while testnum > 1:
  for i in range(2, testnum + 1):
    if testnum % i == 0:
      testnum = testnum // i
      if testnum == 1:
        print(i)
        break
# 6857