from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0] * m for i in range(n)]
        queue = deque()

        cnt_fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    vis[i][j] = 2
                if grid[i][j] == 1:
                    cnt_fresh += 1
        
        tm = 0
        cnt = 0
        delrow = [-1, 0, +1, 0]
        delcol = [0, +1, 0, -1] 
        while queue:
            r, c, t = queue.popleft()
            tm = max(tm, t)

            for i in range(4):
                row = r + delrow[i]
                col = c + delcol[i]
                if row >= 0 and row < n and col >= 0 and col < m and vis[row][col] == 0 and grid[row][col] == 1:
                    vis[row][col] = 2
                    queue.append((row, col, t + 1))
                    cnt += 1

        if cnt != cnt_fresh:
            return -1
        
        return tm
