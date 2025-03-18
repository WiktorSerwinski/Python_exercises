def find_first_rep(nums: list[int]):
    pom: dict = {}
    for i in range(0,len(nums)):
       pom[nums[i]] = pom.get(nums[i],0) +1
       if(pom[nums[i]] >1):
           return nums[i]
    
def del_rep(nums: list[int]):
    pom: dict = {}
    for i in range(0,len(nums)):
       pom[nums[i]] = pom.get(nums[i],0) +1
    no_rep =[]
    for key,value in pom.items():
        if(value == 1):
            no_rep.append(key)
    no_rep.sort()
    return no_rep

        



# nums = [4, 5, 4, 11, 4, 5, 1, 2, 4]


# print(del_rep(nums))






def is_balanced(word: str)->bool:
    count =0    
    for w in word:
        if(w == "("):
            count+=1
        if(w == ")"):
            count-=1     
        if(count < 0):
            return False
    if(count==0):
        return True
    else:
        return False
    
def is_anagram(word1: str, word2: str)->bool:
    if(len(word1)==len(word2)):
        word1 = sorted(word1)
        word2 = sorted(word2)
        if(word1==word2):
            return True
        else:
            return False
    else:
        return False
    
def is_prime(x: int)->bool:
    for i in range(x):
        if(x%(i+1)==0 and i+1!=1 and i+1!=x):
            return False
    return True
        
def gcd(x: int, y: int):
    num = 1
    for i in range(1,min(x,y)+1):
        if x%i == 0 and y%i==0 and i>num:
            num = i
    return num
    
    
def Fib(n: int):
    x0 = 1
    x1 = 1
    for _ in range(2,n):
        xpom = x1
        x1 = x1+x0
        x0 = xpom
    return x1

def Fib_rec(n: int):
    if(n<3):
        return 1
    return Fib_rec(n-1) + Fib_rec(n-2)


def words_count(sentence: str) ->dict[str,int]:
    sentence = sentence.lower()
    sentence = sentence.strip().split()
    dict_word_count = {}
    for word in sentence:
        dict_word_count[word]=dict_word_count.get(word,0)+1
    return dict_word_count

def palindrome(word: str) -> bool:
    word=word.lower()
    if(word==word[::-1]):
        return True
    else:
        return False

from collections import Counter

def count_char(word: str) -> str:
    word = word.replace(" ","")
    word_count = Counter(word)
    print(word_count)
    max = 0
    max_char: str
    for key,val in word_count.items():
        if val>max:
            max = val
            max_char = key
    return max_char
    
def has_duplicate(lst: list):
    d = set()
    for l in lst:
        if l in d:
            return True
        else:
            d.add(l)
    return False
    
    



