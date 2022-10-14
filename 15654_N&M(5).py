n , m = map(int, input().split())
num_list = list(map(int, input().split()))
need_visit = []
num_list.sort()


def dfs(): 
  if m == len(need_visit):
    print(" ".join(map(str,need_visit)))
    return ;
    
  for i in num_list:
    if i not in need_visit:  
      need_visit.append(i);
      dfs();
      need_visit.pop();
  
dfs()