N = int(input())

a = [["A","B","C"], ["D","E","F"], ["G","H","I"]]
result = 0

#check horizontal

def horizontal(arr,column):
    length = 0 
    for i in range(len(arr)-1):
        temp_key = a[i][0][column] 
        if temp_key == a[i+1][0][column]:
            temp_key += 1
        else: 
            length = max(length, temp_key)
            