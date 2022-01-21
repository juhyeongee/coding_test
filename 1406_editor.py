import sys

stack = list(sys.stdin.readline())
how_many = int(sys.stdin.readline())
stack.pop()
index = len(stack) -1


for i in range(how_many):
    order = sys.stdin.readline().strip()
    if order == "L":
        if index <= 0:
            pass
        else:
            index -= 1
    elif order == "D":
        if index < len(stack)-1:
            index += 1 
    elif order == "B":
        del stack[index]
        index -= 1
    else: 
        add = order.split()
        if add[0] == "P" :
            stack.insert(index,add[1])
            index += 1

print("".join(stack))
