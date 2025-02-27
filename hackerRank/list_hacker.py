lista=[]
N = int(input())
for _ in range(N):
    command=input()
    split_comand = command.split()
    if( split_comand[0] == "insert"):
        lista.insert(int(split_comand[1]),int(split_comand[2]))
    elif( split_comand[0] == "print"):
        print(lista)
        
    elif( split_comand[0] == "remove"):
        lista.remove(int(split_comand[1]))
        
    elif( split_comand[0] == "append"):
        lista.append(int(split_comand[1]))
        
    elif( split_comand[0] == "pop"):
        lista.pop()
        
    elif( split_comand[0] == "reverse"):
        lista.reverse()
        
    elif( split_comand[0] == "sort"):
        lista.sort()