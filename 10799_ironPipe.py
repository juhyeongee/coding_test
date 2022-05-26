input_ = list(input())
stack = []

index = 0 
result = 0

for pointer in range(len(input_)):
  if pointer == 0 :
    stack.append("(")
  elif input_[pointer] == "(" :
    stack.append("(")
  elif input_[pointer] == ")":
    stack.pop()
    if input_[pointer-1] == "(":
      result += len(stack)
    else:
      result += 1 

print(result)