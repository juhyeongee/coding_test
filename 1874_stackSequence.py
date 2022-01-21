import sys

n = int(sys.stdin.readline())
n_array = []
stack = []
count = 0 
result = []
error = False;
#for appending stack, made reverse stack
for i in range(n):
    n_array.append(int(i+1))
n_array.reverse()   

for i in range(n):
    input_ = int(input())
    while input_ > count:
        result.append("+")
        count += 1 
        stack.append(count)
    if input_ == stack[-1]:
        stack.pop()
        result.append("-")
    else: 
        error = True;
        break;

if  error==True:
    print("NO")
else:
    print('\n'.join(result))

