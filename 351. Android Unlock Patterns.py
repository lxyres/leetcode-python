class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.count(m,n,0,1,1)
    def count(self,m,n,used,i1,j1):
        if n<=0:
            return 1
        number=0
        if m<=0:
            number=-1
        print(m,n,i1,j1,number,bin(used))
        for i in range(3):
            for j in range(3):
                nextd=used|1<<(i*3+j)
                if nextd!=used:
                    if (i+i1)%2==1 or (j+j1)%2==1 or nextd&1<<(3*(i+i1)//2+(j+j1)//2)!=0:
                        number+=self.count(m-1,n-1,nextd,i,j)
        return number
if __name__ =="__main__":
    print(Solution().numberOfPatterns(1,2))