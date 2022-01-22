import sys 

deque = []

iteration = int(sys.stdin.readline())

for i in range(iteration):
    order = sys.stdin.readline().split()
    if order[0] == "size":
        print(len(deque))
    elif order[0] == "empty":
        if len(deque) == 0 :
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(deque) == 0 :
            print(-1)
        else:
            print(deque[0])
    elif order[0] == "back":
        if len(deque) == 0 :
            print(-1)
        else:
            print(deque[-1])
    elif order[0] == "pop_front":
        if len(deque) == 0 :
            print(-1)
        else: 
            front = deque[0]
            print(front)
            deque = deque[1:]
    elif order[0] == "pop_back":
        if len(deque) == 0 :
            print(-1)
        else:   
            print(deque.pop())

    elif order[0] == "push_front":
        deque.insert(0, order[1])

    elif order[0] == "push_back":
        deque.append(order[1])