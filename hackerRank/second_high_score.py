    
n = int(input())
arr = list(map(int, input().split()))
ranks = list(set(arr))
ranks.sort()
print(ranks)

print(ranks[len(ranks)-2])