def even(n):
    num = 0
    while num <= n:
        yield num
        num += 1
n=int(input())
evens = [str(i) for i in even(n) if i % 2 == 0]
print(",".join(evens))