def fib(n):
    a = 0
    b = 1 
    for i in range(n):
        a , b = b , a+b
    return a

def calc_mean(first, *reminder):
    mean = (first + sum(reminder))/(1+len(reminder))
    return mean
