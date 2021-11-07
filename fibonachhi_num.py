def fib(num):

    prev, cur = 0, 1

    for i in range(1, num):
        prev, cur = cur, prev + cur

    return cur



n = int(input())
print(fib(n))

#Дано целое число  1<=n<=40, вычислить n-ое число Фибоначчи
