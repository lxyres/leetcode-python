class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x:(x[1],x[0]))
        result=[]
        for i in people:
            if i[1]==0:
                result.append(i)
            else:
                start=0
                number=0
                while start<len(result):
                    if result[start][0]>=i[0]:
                        number+=1
                    start+=1
                    if number==i[1]:
                        result.insert(start,i)
                        break
                if number<i[1]:
                    result.insert(start,i)
        return result
if __name__ =="__main__":
    print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))