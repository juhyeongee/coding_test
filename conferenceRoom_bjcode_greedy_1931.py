n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
    data.sort(key = lambda x: x[0])

#일단 리스트로 만드는 데는 성공함 

def solution(data):
    sorted_list = sorted(data)
    last_end = -1 
    conference_count = 0
    
    for i in sorted_list:
        start = i[0]
        end = i[1]
        if start < last_end:
            continue 
        
        if last_end <= end:
            conference_count += 1
            last_end = end
    
    return conference_count

solution(data)