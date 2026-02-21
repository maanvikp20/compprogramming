# 8 kyu - Draw stairs

def draw_stairs(n):
    return "\n".join(" " * i + "I" for i in range(n))

print(draw_stairs(1000))