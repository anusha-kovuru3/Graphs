class Solution:
    def dfs(self, sr, sc, initial_color, ans, new_color, delrow, delcol):
        ans[sr][sc] = new_color
        n = len(ans)
        m = len(ans[0])
        
        for i in range(4):
            row = sr + delrow[i]
            col = sc + delcol[i]
            if row >= 0 and row < n and col >= 0 and col < m and ans[row][col] == initial_color:
                self.dfs(row, col, initial_color, ans, new_color, delrow, delcol)


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]
        if initial_color == color:
            return image
        ans = image
        delrow = [-1, 0, +1, 0]
        delcol = [0, +1, 0, -1]
        self.dfs(sr, sc, initial_color, ans, color, delrow, delcol)
        return ans