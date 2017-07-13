# n = int(input())
# sum = 0;
# for i in range(1,n):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print(sum)

import math


def isprime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


#n = int(input())
n = 10
sum = 0
for i in range(n):
    if isprime(i):
        sum += i
print(sum)
