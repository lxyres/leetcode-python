from collections import deque
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t:
            return 0
        key=list(t)
        left=len(key)
        dic={}
        mini=len(s)+1
        start=0
        end=0
        for i in key:
            if i in dic:
                dic[i].append(-1)
            else:
                dic[i]=deque()
                dic[i].append(-1)
        print(dic)
        for i,w in enumerate(s):
            
            if w in dic:
                if dic[w][0]==-1:
                    left-=1
                dic[w].popleft()
                dic[w].append(i)
                print(dic)
                if left==0:
                    tmp=i
                    for k in dic:
                        tmp=min(tmp,dic[k][0])
                    print (tmp,i,mini)
                    if <mini:
                        
                        mini=tmp-i
                        start=tmp
                        end=i
        if left>0:
            return ""
        return s[start:end+1]
if __name__ == "__main__":
    print(Solution().minWindow("bdab","ab"))