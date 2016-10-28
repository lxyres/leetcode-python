class Solution(object):
    def __init__(self):
        return
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord==endWord:
            return 0
        dic={}
        rdic={}
        n=len(beginWord)
        for i in wordList:
            tmp=self.count(i,endWord)
            rdic[i]=tmp
        s1=[[beginWord,n,1]]
        while s1:
            s2=[]
            for w1 in s1:
                for w2 in rdic:
                    if w2 not in dic:
                        tmp=self.count(w1[0],w2)
                        if tmp==1:
                            if rdic[w2]==0:
                                return w1[2]+1
                            elif rdic[w2]==1:
                                return w1[2]+2
                            elif rdic[w2]<=w2[1]:
                                s2.append([w2,rdic[w2],w1[2]+1])
                                dic[w2]=1
            s1=s2
        return -1
    def count(delf,word1,word2):
        result=0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                result+=1
        return result
if __name__=="__main__":
    print(Solution().ladderLength("hot","dog",["hot","dog"]))