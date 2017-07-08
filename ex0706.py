import math
from itertools import count

def get_num_of_int(x):
    num = 1
    tmp = x % 10
    while tmp != x:
        x = x // 10
        num += 1
        tmp = x % 10
    return num

# def isprime(x):
#     if x <= 1:
#         return False
#     if x == 2:
#         return True
#     bit = get_num_of_int(x)
#     if bit > 1 & (x % 10) in [2,4,5,6,8,0]:
#         return False
#     for i in range(2,int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True


def isprime(n):
    if n <= 1:
        return False
    for i in count(2):
        if i * i > n:
            return True
        if n % i == 0:
            return False

def get_move_circle(x):
    n = get_num_of_int(x)
    l = []
    for i in range(n):
        y = (x % 10) * (10 ** (n-1)) + x // 10
        l.append(y)
        x = y
    return l

n = int(input())
lst = []
for i in range(2,n+1):
    flag = True
    l = get_move_circle(i)
    for j in l:
        if not isprime(j):
            flag = False
            break
    if flag:
        lst.append(i)
print(len(lst))
print(lst)