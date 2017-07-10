def fib(n):
    l = [1,2]
    f = l[-1] + l[-2]
    while f <= n:
        l.append(f)
        f = l[-1] + l[-2]
    return l

n = int(input())
lst = fib(n)
sum = 0
for i in lst:
    if i % 2 == 0:
        sum += i
print(sum)
