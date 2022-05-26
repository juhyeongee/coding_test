
N = int(input())
result  = 1
for i in range(1,N+1):
    result *= i

print(result)



"""
import sys
N = int(input())
sys.setrecursionlimit(10**6)

def factory(a):
    if a == 2:
        return  2
    else:
        return a * factory(a-1)

print(factory(N))"""