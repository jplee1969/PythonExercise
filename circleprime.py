import math
def isprime(x):
    if x <= 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def get_num_of_int(x):
    num = 1
    tmp = x % 10
    while tmp != x:
        x = x // 10
        num += 1
        tmp = x % 10
    return num

def get_move_circle(x):
    n = get_num_of_int(x)
    l = []
    for i in range(n):
        y = (x % 10) * (10 ** (n-1)) + x // 10
        l.append(y)
        x = y
    return l

prime_dic = {}
prime_list = []
n = int(input())
for i in range(2, n + 1):
    prime_dic[i] = 1
for i in range(2, int(n ** .5) + 1):
    for j in range(i * i, n + 1, i):
        if prime_dic[i] == 1:
            prime_dic[j] = 0
for k,v in prime_dic.items():
    if v == 1:
        prime_list.append(k)

lst=[]
for p in prime_list:
    flag = True
    l = get_move_circle(p)
    for j in l:
        if not isprime(j):
            flag = False
            break
    if flag:
        lst.append(i)
print(len(lst))
