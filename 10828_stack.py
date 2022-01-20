import sys


stack = []
N = int(sys.stdin.readline())
for i in range(N):
    input_ = sys.stdin.readline().split()
    order = input_[0]
    #push_pattern = re.compile('(\D*)(\d*)?')
    #m = push_pattern.search(input_)
    # == m = re.match('push \D*', input_)
    #order = m.group(1)
    #push_num = m.group(2)
    
    if order == "push": #띄어쓰기 아  !
        stack.append(input_[1])
    elif order == "top":
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack[-1])
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else: 
            print(0)
    elif order =="size":
        print(len(stack))
    elif order == "pop":
        if len(stack)  == 0:
            print(-1)
        else: 
            print(stack.pop())

