def square(a, b):
    num = a
    while num <= b:
        yield num
        num += 1

a ,b=int(input()),int(input())
print([i*i for i in square(a,b)])