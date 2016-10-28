import functools
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def _cmp(self,s1,s2):
        if s1=="":
            return 1
        if s2=="":
            return -1
        n1=len(s1)
        n2=len(s2)
        print(s1,s2)
        for i in range(min(n1,n2)):
            if ord(s1[i])<ord(s2[i]):
                return 1
            elif ord(s1[i])>ord(s2[i]):
                return -1
        if n1==n2:
            return 0
        elif n1<n2:
            for i in range(n1,n2):
                if s1[i%n1]<s2[i]:
                    return -1
                elif s1[i%n1]>s2[i]:
                    return 1
            return 0
        else:
            for i in range(n2,n1):
                if s1[i]<s2[i%n2]:
                    return -1
                elif s1[i]>s2[i%n2]:
                    return 1
            return 0
        
    def largestNumber(self, nums):
        stt=[str(i) for i in nums]
        stt.sort(key=functools.cmp_to_key(self._cmp))
        result=''
        print(stt)
        for v in stt:
            result+=v
        return result
if __name__=="__main__":
    print(Solution().largestNumber([121,12]))