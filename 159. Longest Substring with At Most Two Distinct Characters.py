class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        now=0
        s1=[]
        s2=[]
        maxi=0
        start=0
        for i,v in enumerate(s):
            print (s1,s2,start)
            if s1 and s1[0]==v:
                s1[1]=i
                continue
            if s2 and s2[0]==v:
                s2[1]=i
                continue
            else:
                if now==0:
                    now+=1
                    s1=[v,i]
                elif now==1:
                    now+=1
                    s2=[v,i]
                else:
                    maxi=max(maxi,i-start)
                    if s1[1]>s2[1]:
                        start=s2[1]+1
                        s2=[v,i]
                    else:
                        start=s1[1]+1
                        s1=[v,i]
        maxi=max(maxi,len(s)-start)
        return maxi
if __name__=="__main__":
    print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))