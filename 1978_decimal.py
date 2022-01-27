import math

n = input()
A = list(map(int, input().split()))
result = []

def sqrt(num):
    return math.floor(num**(1/2)) 

def is_decimal(a):
    if a == 1:
        return False
    cf = []
    for i in range(1, sqrt(a)+1):
        if a % i ==0:
            cf.append(i)
        else:
            pass
    if len(cf) == 1:
        return True 

for j in A:
    if is_decimal(j) == True:
        result.append(j)

print(len(result))
