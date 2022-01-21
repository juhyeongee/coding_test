import sys

stack = list(sys.stdin.readline().strip())
orders = int(sys.stdin.readline())
temp_stack = []


#push와 pop만 이용해서 출력하기!
for i in range(orders):
    order = sys.stdin.readline().strip()
    if order == "L":
        if len(stack) == 0:
            pass
        else:
            temp_stack.append(stack.pop())
    elif order == "D":
        if len(temp_stack)== 0:
            pass
        else:
            stack.append(temp_stack.pop())
    elif order == "B":
        if len(stack) == 0:
            pass
        else:
            stack.pop()
    else: 
        add = order.split()
        if add[0] == "P" :
            stack.append(add[1])

print("".join(stack + list(reversed(temp_stack))))
