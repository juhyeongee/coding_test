import re


def stacker():
    stack = []
    N = input()
    for i in range(int(N)):
        input_ = input()
        push_pattern = re.compile('(\D*)(\d*)?')
        m = push_pattern.search(input_)
        # == m = re.match('push \D*', input_)
        order = m.group(1)
        push_num = m.group(2)

        if order == "push ":
            stack.append(push_num)
        elif order == "top":
            if len(stack) == 0 :
                print(-1)
            else:
                print(stack[-1])
        elif order == "empty":
            if len(stack)  == 0:
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

    return stack;

stacker()