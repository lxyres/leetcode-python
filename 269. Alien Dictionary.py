import queue
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words)==1:
            return words[0]
        dic={}
        ingree={}
        for i in range(len(words)-1):
            print(ingree)
            s1=words[i]
            s2=words[i+1]
            n1=len(s1)
            n2=len(s2)
            if n1<=n2:
                flag=0
                for j in range(n1):
                    if s1[j]!=s2[j] and flag==0:
                        if s1[j] not in dic:
                            dic[s1[j]]=[s2[j]]
                            if s1[j] not in ingree:
                                ingree[s1[j]]=0
                            if s2[j] not in ingree:
                                ingree[s2[j]]=1
                            else:
                                ingree[s2[j]]+=1
                        else:
                            if s2[j] not in dic[s1[j]]:
                                dic[s1[j]].append(s2[j])
                                if s2[j] not in ingree:
                                    ingree[s2[j]]=1
                                else:
                                    ingree[s2[j]]+=1
                        flag=1
                    else:
                        if s1[j] not in ingree:
                            ingree[s1[j]]=0
                        if s2[j] not in ingree:
                            ingree[s2[j]]=0
                for j in range(n1,n2):
                    if s2[j] not in ingree:
                        ingree[s2[j]]=0
            else:
                flag=0
                for j in range(n2):
                    if s1[j]!=s2[j] and flag==0:
                        if s1[j] not in dic:
                            dic[s1[j]]=[s2[j]]
                            if s1[j] not in ingree:
                                ingree[s1[j]]=0
                            if s2[j] not in ingree:
                                ingree[s2[j]]=1
                            else:
                                ingree[s2[j]]+=1
                        else:
                            if s2[j] not in dic[s1[j]]:
                                dic[s1[j]].append(s2[j])
                                if s2[j] not in ingree:
                                    ingree[s2[j]]=1
                                else:
                                    ingree[s2[j]]+=1
                        flag=1
                    else:
                        if s1[j] not in ingree:
                            ingree[s1[j]]=0
                        if s2[j] not in ingree:
                            ingree[s2[j]]=0
                if flag==0:
                    return ""
                for j in range(n2,n1):
                    if s1[j] not in ingree:
                        ingree[s1[j]]=0
        print(ingree)
        size=len(ingree)
        q=queue.Queue()
        for i in ingree:
            if ingree[i]==0:
                q.put(i)
        result=""
        while not q.empty():
            tmp=q.get()
            result+=tmp
            if tmp in dic:
                for i in dic[tmp]:
                    ingree[i]-=1
                    if ingree[i]==0:
                        q.put(i)
        if len(result)==size:
            return result
        else:
            return ""
if __name__=="__main__":
    print(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]))