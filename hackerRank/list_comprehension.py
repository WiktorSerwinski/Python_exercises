if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lista = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                lista.append([i, j, k])
    filtred_list = [x for x in lista if sum(x) != n]

    # print (lista)
    print(filtred_list)
    
