class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result=[]
        former=[]
        value= -2147483648
        for v in nums:
            print(v,result,former)
            former.append(v)
            last=sum(former)
            fsum=sum(former)
            for i,v in enumerate(former[:]):
                if fsum>value:
                    value=fsum+0
                    result=former[i:]
                elif fsum>last:
                    former=former[i:]
                    last=fsum+0
                fsum-=v
        return value
if __name__ == "__main__":
    print(Solution().maxSubArray([0,-3,2,1,-2,3]))