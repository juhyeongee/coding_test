

N = input().split()

num1 = int(N[0])
num2 = int(N[1])
a = max( num1, num2 )
b = min( num1, num2 )
#풀이 2번

while b!= 0:
    a = a % b
    a, b = b, a

print(a)
print(int(num1*num2/a))


'''풀이 1번 
for i in range(min(num1,num2),0,-1):
    if num1 % i == 0 and num2 % i ==0:
        GCF = i
        break

for i in range(max(num1,num2),(num1*num2)+1):
    if i % num1 ==0 and i % num2 == 0:
        LCF = i
        break
    print(GCF)
print(LCF)
'''
