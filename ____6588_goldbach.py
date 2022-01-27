
num = int(input())

cf = []

def is_decimal(a):
    if a == 1:
        return None
    cf = []
    for i in range(1, int(a**(1/2)+1)):
        if a % i ==0:
            cf.append(i)
        else:
            pass
    if len(cf) == 1:
        return a 

lists = [i for i in range(int(num/2))]
decimal_list = []

for i in lists:
    if is_decimal(i) == None:
        pass
    else:
        decimal_list.append(i)

for i in decimal_list:
   if num - i  == True:
       print(i)