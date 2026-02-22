# 6 kyu - Area of n-sided polygon

def area_polygon(vertex):
    sum = 0
    for i in range(len(vertex)):
        x1, y1 = vertex[i]
        x2, y2 = vertex[i - 1]
        sum += x1 * y2 - x2 * y1
    return round(abs(sum / 2), 1)

print(area_polygon([(1, 1), (1, -1), (-1, -1), (-1, 1)]))