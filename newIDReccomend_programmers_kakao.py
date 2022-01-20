def solution (new_id):
    temp = new_id.lower()
    answer = ""

    for i in temp:
        if i ==  '-' or i =='_' or i =='.' or i.isdigit() or i.isalpha():
            answer += i 
        #.. one by one checking & make a variable with adding each numerals. 
    answer = answer + '!'
    
    print(answer)
    for i,c in enumerate(answer):
        if i <= len(answer) -1: 
            while answer[i] == '.' and answer[i+1] == ".":
                answer = answer[:i] + answer[i + 1: ]
    print(answer)
solution("AAsdf134!$$$")