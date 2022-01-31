N = int(input())

a = [["A","B","C"], ["D","E","F"], ["G","H","I"]]
result = 0
for i in range(0,N):
    for j in range(1, N):
        while a[i][j-1] != a[i][j]:
            result += 1
        #a[i-1][j-1], a[i-1][j] = a[i-
        
