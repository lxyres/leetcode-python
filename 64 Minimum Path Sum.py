class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        if n==0:
            return 0
        n=len(grid[0])
        ss=grid[0][0]
        for i in range(1,m):
            grid[i][0]+=ss
            ss=grid[i][0]
        ss=grid[0][0]
        for i in range(1,n):
            grid[0][i]+=ss
            ss=grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]
if __name__ == "__main__":
    print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))