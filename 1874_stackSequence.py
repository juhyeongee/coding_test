import sys

n = int(sys.stdin.readline())
n_array = []
stack = []
result = []
error = False;
#for appending stack, made reverse stack
for i in range(n):
    n_array.append(int(i+1))
n_array.reverse()

stack.append(n_array.pop)
for i in range(n):
    input_ = int(input())
    while input_ > stack[-1]:
        stack.append(n_array.pop)
        result.append("+")
    if input_ == stack[-1]:
        stack.pop()
        result.append("-")
    else: 
        error = True;
        break;

if  error==True:
    print("NO")
else:
    print(result)

