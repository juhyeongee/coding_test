N = int(input())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
listB_copy = sorted(listB[:], reverse= True)
#초기화 해주는 법
result = 0 

temp = sorted(listA)

for j in range(0,N):
    result += temp[j]*listB_copy[j]

print(result)