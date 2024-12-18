from collections import deque
from typing import List

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        # code here
        n =  len(adj)
        visited_array = [False] * n
        queue = deque()
        queue.append(0)
        visited_array[0] = True
        bfs = []
        
        while queue:
            node = queue.popleft()
            bfs.append(node)
            
            for neighbour in adj[node]:
                if visited_array[neighbour] == False:
                    visited_array[neighbour] = True
                    queue.append(neighbour)
        
        return bfs