def mini(a: int, b: int, c: int, d: int):
    return min(min(a,b),min(c,d))

x = input().split(" ")
print(mini(int(x[0]), int(x[1]), int(x[2]), int(x[3])))