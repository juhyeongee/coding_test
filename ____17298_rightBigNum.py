import sys


array = list(map(int, sys.stdin.readline().split()))
stack = []
result = [ -1 for i in range(len(array))]

for i in range(result):
    while stack and array[stack[-1]] < array[i]:
        result[stack.pop()] = array[i]
    stack.append[i]
print(*answer)