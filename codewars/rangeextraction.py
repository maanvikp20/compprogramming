# 4 kyu - Range Extraction

# look if three in order, if so, add to list as "start-end", else add "num"
def solution(args):
    result = []
    i = 0
    while i < len(args):
        start = args[i]
        while i + 1 < len(args) and args[i + 1] == args[i] + 1:
            i += 1
        end = args[i]
        if end - start >= 2:
            result.append(f"{start}-{end}")
        else:
            for num in range(start, end + 1):
                result.append(str(num))
        i += 1
    return ",".join(result)

test = [-3,-2,-1,2,10,15,16,18,19,20]

print(solution(test))