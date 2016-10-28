class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        m=rows
        n=cols
        leng=len(sentence)
        number=0
        now=0
        while m>0:
            if now==leng:
                number+=1
                now=0
            tmp=len(sentence[now])
            if tmp<n:
                n-=(tmp+1)
                now+=1
            elif tmp==n:
                now+=1
                m-=1
                n=cols
            else:
                m-=1
                n=cols
        if now==leng:
            number+=1
        return number
if __name__ =="__main__":
    print(Solution().wordsTyping(["try","to","be","better"],10000,9001))