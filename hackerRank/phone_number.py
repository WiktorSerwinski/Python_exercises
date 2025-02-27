# Enter your code here. Read input from STDIN. Print output to STDOUT
N= int(input())

numbers = []
for _ in range(N):
    num = input()
    if(len(num) == 10 and (num[0] == '7' or num[0] == '8' or num[0] == '9') and num.isdigit()):
        numbers.append([num,"YES"])
    else:
        numbers.append([num,"NO"])

for n in numbers:
    print(n[1])
    