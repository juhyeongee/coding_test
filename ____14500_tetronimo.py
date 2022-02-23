import sys

input = sys.stdin.readline

a = input().split()
n = int(a[0])
m = int(a[1])

array = []
for i in range(n):
    array.append(input().split())

#최댓값 찾기
result_list = []
for i in range(n):
    for j in range(m):
        