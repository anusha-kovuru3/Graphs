class Solution:
    def count(self, n):
        # Code here
        edges = (n*(n - 1)) // 2
        
        return 2 ** edges