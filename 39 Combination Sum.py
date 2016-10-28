class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        result=[]
        for i,v in reversed(list(enumerate(candidates))):
            if v<=target:
                tmp=target
                tmplist=[]
                while(tmp>=v):
                    tmp-=v
                    print('check',tmplist)
                    tmplist.append(v)
                    print(tmplist,tmp,candidates[i+1:])
                    self.Combination(candidates[i+1:],tmplist,tmp,result)
        return result
    def Combination(self,candidates,former,target,result):
        #print(candidates,former,target)
        if target==0:
            result.append(former)
        if not candidates:
            return
        tmplist=former
        tmp=target
        while(tmp>=candidates[0]):
            tmp-=candidates[0]
            tmplist.append(candidates[0])
            self.Combination(candidates[1:],tmplist,tmp,result)
if __name__ == "__main__":
    print(Solution().combinationSum([2,3,6,7],7))