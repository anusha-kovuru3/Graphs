from collections import deque

class Solution:
    def traverse(self, startingNode, vis, isConnected):
        queue = deque()
        queue.append(startingNode)
        vis[startingNode] = True
        while queue:
            node = queue.popleft()
            for i in range(len(isConnected)):
                if isConnected[node][i] == 1 and i != node and not vis[i]:
                    queue.append(i)
                    vis[i] = True

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False] * (n)
        provinces = 0

        for i in range(n):
            if not vis[i]:
                self.traverse(i, vis, isConnected)
                provinces += 1

        return provinces

        