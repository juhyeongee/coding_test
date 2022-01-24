N = int(input())


def lcf(a,b):
    print(a)
    print(b)
    print(type(a))
    while b !=0 : #왜 b가 0이 아닌동안은 되고, a가 0이 아닌동안은 안되지?
        a = a % b
        a,b= b,a
    print(a,b)
    
for i in range(N):
    nums = list(map(int, input().split()))
    print(nums)
    lcf(nums[0],nums[1])
