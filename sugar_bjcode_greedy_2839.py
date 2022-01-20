sugar_kg = int(input())
result = 0 

first_rest_Sugar = sugar_kg % 5
minus_one = 0

if sugar_kg == 1 or sugar_kg == 2 or sugar_kg == 7 or sugar_kg == 4 :
    print(-1)
elif first_rest_Sugar % 3 == 0: 
    result = sugar_kg//5 + first_rest_Sugar//3
    print(result)
elif first_rest_Sugar % 3 != 0:
    while first_rest_Sugar % 3 != 0:
        first_rest_Sugar += 5
        minus_one -= 1
    result = sugar_kg//5 + first_rest_Sugar//3 + minus_one  
    print(result)







"""
if sugar_kg == 1 or 2 or 4 or 7: 
    print(-1)
elif first_rest_Sugar % 3 ==0:
    result = sugar_kg//5
elif first_rest_Sugar % 3 ==1: 
    
box = sugar_kg//5
"""

#5로 나눌 수 있는 만큼 나누고 #3으로 나눠지는지 확인 
#그러고 안나눠지면 5에서 하나 빼봄 
#그러고도 안나눠지면 또 하나 빼봄 
#이걸 거꾸로한다면? 3으로 나눠 떨어질떄까지 안에 들어가 나올 때 박스 수 추가 해
"""
def sugar(kg):
    total_box = 0
    if rest_kg
    rest_kg = kg-5
        
    return total_box + sugar(rest_kg)
#sugar(sugar_kg)

"""

