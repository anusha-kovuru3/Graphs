from typing import List
from collections import deque

class Solution:
    #Function to detect cycle in an undirected graph.
    def detectCycle(self, node, parent, vis, adj):
        vis[node] = True
        
        for num in adj[node]:
            if not vis[num]:
                if self.detectCycle(num, node, vis, adj):
                    return True
            elif parent != num:
                return True
        
        return False       
        
        
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis = [False] * V
		
		for i in range(V):
		    if not vis[i]:
		        parent =  -1
		        if self.detectCycle(i, -1, vis, adj):
		            return True
		return False