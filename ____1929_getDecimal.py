import sys

B = list(map(int, sys.stdin.readline().split()))
result = []

def is_decimal(a):
    if a == 1:
        return False
    cf = set()
    for i in range(1, int(a**(1/2)+1)):
        if a % i ==0:
            cf.add(i)
        else:
            pass
    if len(cf) == 1:
        return True 

for j in range(B[0],B[1]):
    if is_decimal(j) == True:
        print(j)