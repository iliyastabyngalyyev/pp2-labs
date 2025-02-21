def squares(n):
    num = 0
    while num <= n:
        yield num
        num += 1
n=int(input())
print([i*i for i in squares(n)])