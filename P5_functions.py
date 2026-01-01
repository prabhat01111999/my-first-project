def fib(n):
    a = 0
    b = 1 
    for i in range(n):
        a , b = b , a+b
    return a

t = fib(2000)
print(t)

def calc_mean(first, *reminder):
    mean = (first + sum(reminder))/(1+len(reminder))
    return mean


#Recursion

def fib_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    return fib_2(n-1) + fib(n-2)

x = fib_2(2000)
print(x)
