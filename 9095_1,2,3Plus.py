itr = int(input())

for i in range(itr):
    n = int(input())
    result = [1 for i in range(n+1)]
    for i in range(2,n+1):
        if i == 2 :
            result[i] = 2  
        else:
            result[i] =  result[i-1] + result[i-2] + result[i-3]
    print(result[n])
    