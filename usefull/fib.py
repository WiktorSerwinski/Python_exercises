# 1 1 2 3 5 8 13 21 

def fib(n):
    x = [1, 2]
    if(n>=0):
        if(n<=2):
            print(1)
            return        
        for i in range(3,n):
            xp = x[1]
            x[1] = x[0] + x[1]
            x[0] = xp
        print(x[1])
    print("401 Fault")

def fibo(n):
    fib_list= [1,1]
    for i in range(2,n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
    for f in fib_list:
        print(f)






def fibonacci():
    n = int(input("Podaj liczbe wyrazow ciagu > "))
    x1,x2=1,1
    if(n<2):
        print(f"Fib[1]: {x1}")
    print(f"Fib[1]: {x1}")
    print(f"Fib[2]: {x2}")
    sum= x1+x2
    for i in range(2,n):
        x_pom=x2
        x2 = x1 + x2
        x1 = x_pom
        sum+=x2        
        print(f"Fib[{i+1}]: {x2}")
    print(sum)
# fib(int(input("Podaj n wyrazow ciągu")))
fibonacci()
    
    