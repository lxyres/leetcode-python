class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result =set()
        s1=[]
        for v in candidates:
            s2=[]
            print(v,s1,result)
            if v==target:
                result.add(tuple([v]))
            elif v < target:
                for w in s1:
                    if w[-1]+v < target:
                        ww= w+[v+w[-1]]
                        ww[-2]=v
                        s2.append(w)
                        s2.append(ww)
                    elif w[-1]+v==target:
                        s2.append(w)
                        ww=w[:-1]
                        ww.append(v)
                        ww.sort()
                        result.add(tuple(ww))
                    else:
                        s2.append(w)
                s2.append([v,v])
                s1=s2
        rr= [list(i) for i in result]
        rr.reverse()
        return rr
if __name__ == "__main__":
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5],8))