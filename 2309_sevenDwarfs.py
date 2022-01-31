a = [int(input()) for i in range(9)]


total = sum(a)
for i in range(len(a)):
    b = list(a)
    b.remove(a[i])
    #print(b)
    for j in range(len(b)):
        if total - (a[i]+b[j]) == 100:
            n, m = a[i],b[j]
            break

a.remove(n)
a.remove(m)
a.sort()
for i in a:
    print(i)