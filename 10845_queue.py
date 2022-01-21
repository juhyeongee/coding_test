import sys

orders = int(sys.stdin.readline())
queue = []

for i  in range(orders):
    order = sys.stdin.readline().split()
    if order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        print(queue[0])
    elif order[0] == "back":
        print(queue[-1])
    elif order[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            rtn = queue[0]
            print(rtn)
            queue = queue[1:]
    elif order[0] == "push":
        queue.append(int(order[1]))



