

N = int(input())
result = 0

five = 0
for i in range(1,N+1):
    if i % 5 == 0:
        while i % 5 == 0:
            five += 1
            i = i / 5

print(int(five))