n , m = map(int, input().split())

need_visit = []

def dfs(): 
  if m == len(need_visit):
    print(" ".join(map(str,need_visit)))
    return ;
    
  for i in range(1, n+1):
    if len(need_visit) != 0 :
      if i < need_visit[-1] :  
        continue;
    need_visit.append(i);
    dfs();
    need_visit.pop();
  
dfs()