from queue import Queue
import sys
import time 

start= time.time()
#trial= 0 
#que = Queue()

input_ = sys.stdin.readline().split()
num_list = list(range(1, int(input_[0])+1))
increase = int(input_[1])
index = 0
result = []
#index와 increase는 분리되었어야 했다. 이게 분리가 안되니까 계속 머릿속에서 돌았던거
while len(num_list) != 0:
    index =+ increase -1
    if index >= len(num_list):
        index = index % len(num_list)
        
    result.append(num_list.pop(index))

print(result)

""" Queue import 안하고 풀기.. queue때문에 늦어지는 것 같긴함
for i in range(len(num_list)):
    que.put(num_list[i])

while len(result) != len(num_list):
    trial += 1
    if trial % order == 0:
        result.append(que.get())
    else:
        que.put(que.get())
"""
#que 리스트로 만드는 법 list(que.queue)
#pop(n)


end = time.time()

print(f"{end - start:.5f} sec")