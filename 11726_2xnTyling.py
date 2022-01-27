n = int(input())

result = [1 for _ in range(n+1)]

for i in range(2,n+1):
    result[i] = result[i-1] + result[i-2]

print(result[n]%10007)