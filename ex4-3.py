def hanoi(n, A, B, C):
    if n == 1:
        print('Move', n, 'from', A, 'to', C)
    else:
        hanoi(n - 1, A, C, B)
        print('Move', n, 'from', A, 'to', C)
        hanoi(n - 1, B, A, C)


num = int(input())
hanoi(num, 'A', 'B', 'C')