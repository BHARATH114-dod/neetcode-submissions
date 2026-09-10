class Solution:
    def climbStairs(self, n: int) -> int:
        hash = {}
        def dfs(i):
         if i > n:
            return 0
         if i == n:
            return 1
         if i in hash:
            return hash[i]
         hash[i] = dfs(i +2) + dfs(i+1)
         return hash[i]
        return dfs(0)