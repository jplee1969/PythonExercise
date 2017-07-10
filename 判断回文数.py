# def is_palin(x):
#     if str(x) == str(x)[::-1]:
#         return True
#     else:
#         return False

def is_palin(x):
    y = 0
    t = x
    while x // 10 != 0:
        y = y * 10 + (x % 10) * 10
        x = x // 10
    y = y + x
    return y == t

x = int(input())
print(is_palin(x))