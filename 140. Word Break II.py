from collections import deque
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord=False
        self.next={}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        tmp=self.root
        for i in word:
            if i not in tmp.next:
                tmp.next[i]=TrieNode()
            tmp=tmp.next[i]
        tmp.isWord=True
    def search(self,word,start):
        result=[]
        self.pair(word,start,self.root,result)
        return result
    def pair(self,word,start,root,result):
        if root.isWord==True:
            result.append(start)
        if start==len(word):
            return
        for i in root.next:
            if word[start]==i:
                self.pair(word,start+1,root.next[i],result)  
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not s or not wordDict:
            return []
        trie=Trie()
        leng=[]
        for i in wordDict:
            trie.insert(i)
            leng.append(len(i))
        result=deque()
        maxi=max(leng)
        mini=min(leng)
        s2=trie.search(s,0)
        for i in range(maxi):
            if i+mini in s2:
                result.append([s[:i+mini]])
            else:
                result.append([])
        print(result)
        for i in range(mini,len(s)):
            s1=result[0]
            if not s1:
                result.popleft()
                result.append([])
            else:
                s2=trie.search(s,i)
                result.append([])
                if not s2:
                    result.popleft()
                    continue
                for word in s1:
                    for j in s2:
                        result[j-i].append(word+" "+s[i:j])
                result.popleft()
            print(result)
        return result[0]
if __name__ =="__main__":
    print(Solution().wordBreak("apple",["pear","apple","peach"]))