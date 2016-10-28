class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        result=[]
        while len(s)!=0:
            index=0
            flag=0
            while index<len(s):
                if s[index]==' ':
                    if index!=0:
                        result.append(s[:index])
                    s=s[index+1:]
                    flag=1
                    break
                else:
                    index+=1
            if flag==0 and index==len(s):
                print("wtd",s,len(s))
                result.append(s)
                break
        print(result)
        result.reverse()
        r=result[0]
        for i in result[1:]:
            r+=' '
            r+=i
        return r
if __name__=="__main__":
    print("start",Solution().reverseWords("     a          "),"end")