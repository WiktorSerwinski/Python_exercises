from functools import reduce


def divide(x,y):
    try:
        result=x//y
        return result
    except Exception as e:
        print(e)
        
def prime_number(x):
    for i in range(1,x):
        if(x%i==0):
            return False
    return True

def factorial_number(x):
    for i in range(x-1,1,-1):
        x*=i
    return x

def factorial_rec(x):
    if(x==1 or x==0):
        return 1
    else:
        return x*factorial_rec(x-1)

def fib(n):
    fib_list=[1,1]
    if(n<=2):
        print(fib_list)
    else:
        for i in range(2,n):
            fib_list.append(fib_list[i-1]+fib_list[i-2])
        print(fib_list)


def fib_rec(n):
    return n if n<2 else fib_rec(n-1)+fib_rec(n-2)
    
print(fib_rec(10))    
        