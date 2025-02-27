arr=[2,45,63,12,23]
arr1 = []

def rot(arr):
    rev_arr=[]
    for i in range(len(arr)-1,-1,-1):
        rev_arr.append(arr[i])
    return rev_arr

def last_first(arr):
    pom = arr[len(arr)-1]
    arr[len(arr)-1] = arr[0]
    arr[0] = pom
    return arr    

def rev_string(str):
    str = str[::-1]
    return str

def rev_words(words: str):
    l = words.split()
    l = l[::-1]
    words = (" ").join(l)
    print(words)
    
def count_words(text: str):
    text = text.split()   
    print(text)
    d ={}
    for t in text:
        if(t in d):
            d[t]+=1 
        else:
            d[t]=1
    print(d)






def sum_dic(dic: dict):
    sum = 0
    for _,value in dic.items():
        sum+=value
    return sum

from collections import defaultdict

def duplicate_value(dic: dict):
    a = defaultdict(list)
    for key,value in dic.items():
        a[value].append(key)
    print(a)
    


dic = {'a': 200, 'b': 300, 'c': 300}
duplicate_value(dic)















