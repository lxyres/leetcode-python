class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        if not board[0]:
            return
        m=len(board)
        n=len(board[0])
        if m==1:
            if n==1:
                board[0][0]=0
                return 
            else:
                if board[0][0]==1:
                    board[0][0]=2
                if board[0][n-1]==1:
                    board[0][n-1]=2
                for i in range(n):
                    if board[0][i]==0 :
                        if i!=0 and board[0][i-1]==1:
                            board[0][i-1]=2
                        if  i!=n-1 and board[0][i+1]==1:
                            board[0][i+1]=2
                for i in range(n):
                    if board[0][i]==2:
                        board[0][i]=0
                return
        if n==1:
            if m==1:
                board[0][0]=0
                return 
            else:
                if board[0][0]==1:
                    board[0][0]=2
                if board[m-1][0]==1:
                    board[m-1][0]=2
                for i in range(m):
                    if board[i][0]==0 :
                        if i!=0 and board[i-1][0]==1:
                            board[i-1][0]=2
                        if  i!=m-1 and board[i+1][0]==1:
                            board[i+1][0]=2
                for i in range(n):
                    if board[i][0]==2:
                        board[i][0]=0
                return
        for i in range(m):
            for j in range(n):
                tmp=0
                if i==0:
                    if j==0:
                        if board[i+1][j]==1 or board[i+1][j]==2:
                            tmp+=1
                        if board[i][j+1]==1 or board[i][j+1]==2:
                            tmp+=1
                        if board[i+1][j+1]==1 or board[i+1][j+1]==2:
                            tmp+=1
                    elif j==n-1:
                        if board[i+1][j]==1 or board[i+1][j]==2:
                            tmp+=1
                        if board[i][j-1]==1 or board[i][j-1]==2:
                            tmp+=1
                        if board[i+1][j-1]==1 or board[i+1][j-1]==2:
                            tmp+=1
                    else:
                        if board[i+1][j]==1 or board[i+1][j]==2:
                            tmp+=1
                        if board[i][j+1]==1 or board[i][j+1]==2:
                            tmp+=1
                        if board[i+1][j+1]==1 or board[i+1][j+1]==2:
                            tmp+=1
                        if board[i][j-1]==1 or board[i][j-1]==2:
                            tmp+=1
                        if board[i+1][j-1]==1 or board[i+1][j-1]==2:
                            tmp+=1
                elif i==m-1:
                    if j==0:
                        if board[i-1][j]==1 or board[i-1][j]==2:
                            tmp+=1
                        if board[i][j+1]==1 or board[i][j+1]==2:
                            tmp+=1
                        if board[i-1][j+1]==1 or board[i-1][j+1]==2:
                            tmp+=1
                    elif j==n-1:
                        if board[i-1][j]==1 or board[i-1][j]==2:
                            tmp+=1
                        if board[i][j-1]==1 or board[i][j-1]==2:
                            tmp+=1
                        if board[i-1][j-1]==1 or board[i-1][j-1]==2:
                            tmp+=1
                    else:
                        if board[i-1][j]==1 or board[i-1][j]==2:
                            tmp+=1
                        if board[i][j+1]==1 or board[i][j+1]==2:
                            tmp+=1
                        if board[i-1][j+1]==1 or board[i-1][j+1]==2:
                            tmp+=1
                        if board[i][j-1]==1 or board[i][j-1]==2:
                            tmp+=1
                        if board[i-1][j-1]==1 or board[i-1][j-1]==2:
                            tmp+=1
                else:
                    if j==0:
                        if board[i-1][j]==1 or board[i-1][j]==2:
                            tmp+=1
                        if board[i-1][j+1]==1 or board[i-1][j+1]==2:
                            tmp+=1
                        if board[i][j+1]==1 or board[i][j+1]==2:
                            tmp+=1
                        if board[i+1][j+1]==1 or board[i+1][j+1]==2:
                            tmp+=1
                        if board[i+1][j]==1 or board[i+1][j]==2:
                            tmp+=1
                    elif j==n-1:
                        if board[i-1][j]==1 or board[i-1][j]==2:
                            tmp+=1
                        if board[i-1][j-1]==1 or board[i-1][j-1]==2:
                            tmp+=1
                        if board[i][j-1]==1 or board[i][j-1]==2:
                            tmp+=1
                        if board[i+1][j-1]==1 or board[i+1][j-1]==2:
                            tmp+=1
                        if board[i+1][j]==1 or board[i+1][j]==2:
                            tmp+=1
                    else:
                        if board[i-1][j-1]==1 or board[i-1][j-1]==2:
                            tmp+=1
                        if board[i-1][j]==1 or board[i-1][j]==2:
                            tmp+=1
                        if board[i-1][j+1]==1 or board[i-1][j+1]==2:
                            tmp+=1
                        if board[i][j+1]==1 or board[i][j+1]==2:
                            tmp+=1
                        if board[i+1][j+1]==1 or board[i+1][j+1]==2:
                            tmp+=1
                        if board[i+1][j]==1 or board[i+1][j]==2:
                            tmp+=1
                        if board[i+1][j-1]==1 or board[i+1][j-1]==2:
                            tmp+=1
                        if board[i][j-1]==1 or board[i][j-1]==2:
                            tmp+=1
                print(i,j,board[i][j],tmp)
                if board[i][j]==0 and tmp==3:
                    board[i][j]=3
                elif board[i][j]==1:
                    if tmp!=2 and tmp!=3:
                        board[i][j]=2
        print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j]>1:
                    board[i][j]-=2
if __name__=="__main__":
    m=[[1,1],[1,0]]
    print(Solution().gameOfLife(m))
    print(m)