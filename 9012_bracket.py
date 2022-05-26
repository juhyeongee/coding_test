import sys 
N = int(sys.stdin.readline())

def check():
    brackets = sys.stdin.readline()
    splited_brackets = list(brackets)
    splited_brackets.pop()

    stack = []
    try: 
        for i in splited_brackets:
            if i == "(":
                stack.append(i)
            elif i == ")":
                stack.pop()

        if len(stack) == 0:
            print("YES")
        else: 
            print("NO")
    except:
        print("NO")

for i in range(N):
    check()