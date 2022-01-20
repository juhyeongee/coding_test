#greedy_2
N = int(input())
time_list = list(map(int, input().split()))

sorted_time_list = sorted(time_list)
result = 0 
for i in range(len(sorted_time_list)+1):
    result += sum(sorted_time_list[0:i])

print(result)