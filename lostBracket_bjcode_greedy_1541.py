import re
expression = input()

#____second_try_____ 
minus_index = expression.find("-")

print(minus_index)


""" 
___first_try____


#플러스로 먼저 split 하고 
#앞에 -가 붙어있는 것 이후로 계쏙 더하다가 -가 없어지면 없애볼까? 


firstSplited = expression.split("-")
print(firstSplited)
for i in firstSplited:
    if i.find("+") != -1:
        temp_list = i.split("+")
        secondSplited = [int(x) for x in temp_list]
        print(secondSplited)
    else: 
        pass
"""