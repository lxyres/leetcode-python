class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic={}
        for i,v in enumerate(equations):
            if v[0] not in dic:
                dic[v[0]]=[{},{}]
                dic[v[0]][1][v[1]]=values[i]
            else:
                dic[v[0]][1][v[1]]=values[i]
            if v[1] not in dic:
                dic[v[1]]=[{},{}]
                dic[v[1]][1][v[0]]=values[i]
            else:
                dic[v[1]][1][v[0]]=values[i]
        count=1
        while count!=0:
            count=0
            for word in dic:
                tmp={}
                for i in dic[word][1]:
                    if i in dic:
                       for j in dic[i][0]:
                           if j!=word and j not in dic[word][0] and j not in dic[word][1]:
                                tmp[j]=dic[word][1][i]*dic[i][0][j]
                       for j in dic[i][1]:
                           if j!=word and j not in dic[word][0] and j not in dic[word][1]:
                                tmp[j]=dic[word][1][i]*dic[i][1][j]
                    dic[word][0][i]=dic[word][1][i]
                count+=len(tmp)
                dic[word][1]=tmp
        result=[]
        print(dic)
        for i in queries:
            if i[0]==i[1]:
                result.append(1.0)
            elif i[0] in dic and i[1] in dic[i[0]][0]:
                result.append(dic[i[0]][0][i[1]])
            else:
                result.append(-1.0)
        return result
if __name__ =="__main__":
     print(Solution().calcEquation([["a","b"],["b","c"] ],[2.0,3.0],[ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]))