from time import time
from BFS import bfs
from node import Node

initial_state= [3,3,1]

Node.num_of_instances=0
t0=time()
solution=bfs(initial_state)
t1=time()-t0
print('Solution:', solution)
print('space:',Node.num_of_instances)
print('time:',t1)


