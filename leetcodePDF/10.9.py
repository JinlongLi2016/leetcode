def dfs(nleft, nright, state, path, result):
  '''
  nleft:
  '''
  if nleft==0 and nright==0:	
  	result.append(path) 
  	return 
  if nleft > 0:
    dfs(nleft-1, nright, state+1, path + '(', result)
  if nright > 0 and state > 0:
    dfs(nleft, nright-1, state-1, path+')', result)

r = []
dfs(3, 3, 0, '', r)
print(r)