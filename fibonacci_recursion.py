def fibonacci_no(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_no(num - 2) + fibonacci_no(num - 1)

n = 7
for i in range(n):
    print(fibonacci_no(i), end=' ')
