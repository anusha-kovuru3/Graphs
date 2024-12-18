class Solution:
    def dfs(self, node, vis, adj, dfs_ans):
        vis[node] = True
        dfs_ans.append(node)
        
        for num in adj[node]:
            if not vis[num]:
                self.dfs(num , vis, adj, dfs_ans)
                
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        n = len(adj)
        dfs_ans = []
        vis = [False] * n
        
        self.dfs(0, vis, adj, dfs_ans)
        return dfs_ans