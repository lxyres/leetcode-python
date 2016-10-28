class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n<=0:
            return []
        global cacheTable
        cacheTable={}
        return self.generate(1,n+1)
    def generate(self,start,end):
        if start==end:
            return [None]
        if  (start,end) in cacheTable:
            return cacheTable[(start,end)]
        root=[]
        for i in range(start,end):
            for left in self.generate(start,i):
                for right in self.generate(i+1,end):
                    tmp=TreeNode(i)
                    tmp.left=left
                    tmp.right=right
                    root.append(tmp)
        cacheTable[(start,end)]=root
        return cacheTable[(start,end)]

if __name__ == "__main__":
    print(Solution().generateTrees(3))