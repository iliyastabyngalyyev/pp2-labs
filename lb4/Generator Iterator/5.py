def n_to_0(n):
    num = n
    while num != -1:
        yield num
        num -= 1
n=int(input())
print([i for i in n_to_0(n)])