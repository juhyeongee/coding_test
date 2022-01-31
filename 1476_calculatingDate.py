import sys
date = list(map(int, sys.stdin.readline().split()))


the_day = [[1,1,1]]
first_day = [1,1,1]
while date not in the_day:
    the_day.append(first_day)
    if first_day[0] < 15:
        first_day[0] += 1
    else:
        first_day[0] = 1
    if first_day[1] < 28:
        first_day[1] += 1
    else:
        first_day[1] = 1
    if first_day[2] < 19:
        first_day[2] += 1
    else:
        first_day[2] = 1
print(len(the_day))
    