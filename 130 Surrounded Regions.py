class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m=len(board)
        if m==0:
            return
        n=len(board[0])
        if n==0:
            return
        result=[]
        for i in board:
            print(i)
        print("")
        for i in range(n):
            if board[0][i]=='O':
                board[0][i]='M'
                result.append([0,i])
        for i in range(1,m-1):
            if board[i][n-1]=='O':
                board[i][n-1]='M'
                result.append([i,n-1])
        for i in range(n-1,-1,-1):
            if board[m-1][i]=='O':
                board[m-1][i]='M'
                result.append([m-1,i])
        for i in range(m-2,0,-1):
            if board[i][0]=='O':
                board[i][0]='M'
                result.append([i,0])
        while result:
            v=result.pop()
            if v[0]>0:
                if board[v[0]-1][v[1]]=='O':
                    board[v[0]-1][v[1]]='M'
                    result.append([v[0]-1,v[1]])
            if v[0]<m-1:
                if board[v[0]+1][v[1]]=='O':
                    board[v[0]+1][v[1]]='M'
                    result.append([v[0]+1,v[1]])
            if v[1]>0:
                if board[v[0]][v[1]-1]=='O':
                    board[v[0]][v[1]-1]='M'
                    result.append([v[0],v[1]-1])
            if v[1]<n-1:
                if board[v[0]][v[1]+1]=='O':
                    board[v[0]][v[1]-1]='M'
                    result.append([v[0],v[1]+1])
        for i in board:
            print(i)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='M':
                    board[i][j]='O'
                else:
                    board[i][j]='X'

        
if __name__=="__main__":
    tmp=["OXXOX","XOOXO","XOXOX","OXOOO","XXOXO"]
    tmp=[list(i) for i in tmp]
    print(Solution().solve(tmp))