

a = list(map(int, input().split()))
n = len(a)
result = []

for i in range(1,n):
    if i == 1:
        result.append(a[0])
    else:
        maxlist = []
        for j in range(1,n//2+1):
            maxlist.append(a[n-j]+a[j])
        result.append(maxlist)


print(result)
