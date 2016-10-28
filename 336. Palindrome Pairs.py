class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord=-1
        self.next={}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word,index):
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
        tmp.isWord=index
            
        

    def search(self,root):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        result=[]
        self._search(root,"",result)
        print("search")
        return result
    def _search(self,root,former,result):
        print("check")
        if root.isWord!=-1:
            result.append((former,root.isWord))
        if root.next:
            for i in root.next:
                self._search(root.next[i],former+i,result)
        
    def findpair(self, word):
        result=[]
        self._findpair(word,0,self.root,result)
        print("finished")
        return result
    def _findpair(self,word,start,root,result):
        print(root.isWord)
        if start==len(word):
            tmp=self.search(root)
            print("check1")
            if tmp:
                print(tmp)
                for k in tmp:
                    if self.isPa(k[0])==True:
                        print(k)
                        result.append(k[1])
            print("prepare to end")
            return
        if root.isWord!=-1:
            if self.isPa(word[start:]):
                result.append(root.isWord)
        print(word,start)
        if word[start] in root.next:
            self._findpair(word,start+1,root.next[word[start]],result)
            return
        
    def isPa(self,word):
        print("pa check",word)
        i=0
        j=len(word)-1
        while i<j:
            if word[i]!=word[j]:
                return False
            else:
                i+=1
                j-=1
        return True
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        trie=Trie()
        if len(words)<2:
            return []
        for i,v in enumerate(words):
            trie.insert(v[::-1],i)
        result=[] 
        for i,v in enumerate(words):
            print(i,v,"start")
            s2=trie.findpair(v)
            print(i,v,"end")
            if not s2:
                continue
            else:
                for j in s2:
                    if j!=i:
                        result.append([i,j])
        print("??")
            
        return result
if __name__ =="__main__":
     print(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]))