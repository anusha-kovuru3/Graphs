from typing import List
from collections import deque

class Solution:
    def detectCycle(self, startingNode, vis, adj):
        queue = deque()
        queue.append((startingNode, -1))
        vis[startingNode] = True
        
        while queue:
            node, parent = queue.popleft()
            for num in adj[node]:
                if not vis[num]:
                    vis[num] = True
                    queue.append((num, node))
                elif parent != num:
                    return True
        return False
    
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    vis = [False] * V
		
	    for i in range(V):
		    if not vis[i]:
		        if self.detectCycle(i, vis, adj):
		            return True
		
		return False
		