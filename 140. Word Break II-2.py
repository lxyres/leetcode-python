from collections import defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """

        if not s or not wordDict:
            return []
        precheck={}
        for word in wordDict:
            for i in word:
                if i not in precheck:
                    precheck[i]=True
        for i in s:
            if i not in precheck:
                return []
        del precheck
        leng=[]
        dic={}
        for i in wordDict:
            dic[i]=len(i)
            leng.append(len(i))
        result=defaultdict(list)
        maxi=max(leng)
        mini=min(leng)
        for i in range(mini,maxi+1):
            if s[:i] in dic:
                result[i].append(s[:i])
        for i in range(len(s)):
            print(result[i])
        print("end")
        for i in range(mini,len(s)+1-mini):
            print(i,result[i])
            if not result[i]:
                continue
            for j in dic:
                if s[i:i+len(j)]==j:
                    for former in result[i]:
                        result[i+len(j)].append(former+" "+j)
            result[i].clear()
        return result[len(s)]
if __name__ =="__main__":
    print(Solution().wordBreak("catsanddog",["cat","cats","and","sand","dog"]))