def d_3_4(n):
    num = 0
    while num <= n:
        yield num
        num += 1
n=int(input())
print([i for i in d_3_4(n) if i % 3 == 0 and i % 4 == 0])