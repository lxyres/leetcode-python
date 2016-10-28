class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        height=[0 for i in range(n)]
        maxi=0
        for line in matrix:
            for i,v in enumerate(line):
                if v=="0":
                    height[i]=0
                else:
                    height[i]+=1
            maxi=max(maxi,self.maxAreaInHist(height))
        return maxi
    def maxAreaInHist(self,Hist):
        stack=[]
        maxi=0
        n=len(Hist)
        for i,v in enumerate(Hist):
            if not stack:
                stack.append((i,v))
                maxi=max(maxi,v)
            else:
                tmps=i
                while stack and stack[-1][1]>=v:
                    tmp=stack.pop()
                    tmps=tmp[0]
                    maxi=max(maxi,tmp[1]*(i-tmp[0]))
                stack.append((tmps,v))
        while stack:
            tmp=stack.pop()
            maxi=max(maxi,tmp[1]*(n-tmp[0]))
        return maxi
if __name__ == "__main__":
    print(Solution().maximalRectangle(["01101","11010","01110","11110","11111","00000"]))