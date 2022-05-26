
n = int(input())
if n == 1 : 
    print(1)

else:
    result = [1 for _ in range(n+1)]
    result[2]=3
    for i in range(3,n+1):
        result[i] = result[i-1] + 2*(result[i-2])

    print(result[n]%10007)