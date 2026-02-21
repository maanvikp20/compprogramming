# 4 kyu - magnet particules in boxes

def doubles(maxk, maxn):
    sum = 0
    for n in range(1, maxn+1):
        base = (n+1)**2
        power = 1/base
        for k in range(1, maxk+1):
            sum += power/k
            power /= base

    return sum

print(doubles(10000, 1000))
    

