class Solution(object):
    def __init__(self):
        def countone(i):
            number=0
            while i>0:
                i-=i&-i
                number+=1
            return number
        self.shi={}
        for i in range(13):
            number=countone(i)
            if number not in self.shi:
                self.shi[number]=[str(i)]
            else:
                self.shi[number].append(str(i))
        self.fen={}
        for i in range(61):
            number=countone(i)
            v=str(i)
            v=(2-len(v))*"0"+v
            if number not in self.fen:
                self.fen[number]=[v]
            else:
                self.fen[number].append(v)
        print(self.shi)
        print(self.fen)
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result=[]
        for i in range(num+1):
            if i not in self.shi:
                break
            s1=self.shi[i]
            if num-i not in self.fen:
                continue
            s2=self.fen[num-i]
            for a in s1:
                for b in s2:
                    result.append(a+":"+b)
        return result
if __name__ =="__main__":
    print(Solution().readBinaryWatch(2))