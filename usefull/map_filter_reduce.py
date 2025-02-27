from functools import reduce
from fib import fib

def map_train(lista):
    # return [x * 2 for x in list]
    return list(map(lambda x: x*2,lista))
    

def filter_train(lista):
    # return [x for x in list if x %2 == 0]
    return list(filter(lambda x: x % 2 == 0, lista))

def reduce_list(lista):
    return reduce(lambda acc, n: acc*n,lista)

    
lista = [1,2,3,4,5]
print(reduce_list(lista))


# x = lambda a,b: a+b



# print((lambda a,b: a+b)(1,2))
# print(x(lista[0],lista[1]))


# print(filter_train(lista))
# print(map_train(lista))