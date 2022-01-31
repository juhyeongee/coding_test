import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
s = list(input().strip())

def check(num):
    num = list(str(num))
    for i in num:
        if i in s: 
            return False
    return True

result = abs(n-100)
print(result)
print(check(234))
            