from queue import Queue
import sys
import time 

start= time.time()
trial= 0 
que = Queue()

input_ = sys.stdin.readline().split()
num_list = list(range(1, int(input_[0])+1))
order = int(input_[1])

result = []

for i in range(len(num_list)):
    que.put(num_list[i])

while len(result) != len(num_list):
    trial += 1
    if trial % order == 0:
        result.append(que.get())
    else:
        que.put(que.get())
#que 리스트로 만드는 법 list(que.queue)

print(result)

end = time.time()

print(f"{end - start:.5f} sec")