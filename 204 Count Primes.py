import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        result=[1 for i in range(n-1)]
        result[0]=0
        result[1]=1
        prime=[]
        for i in range(2,int(math.sqrt(n))+1):
            print(result)
            if result[i-1]!=0:
                for j in prime:
                    if i%j==0:
                        result[i-1]=0
                        break
                if result[i-1]!=0:
                    prime.append(i)
                    s1=1
                    for k in prime:
                        s1*=k
                    tmp=s1+i
                    while(tmp)<n:
                        result[tmp-1]=0
                        tmp+=s1
        print(result)
        return sum(result)
if __name__=="__main__":
    print(Solution().countPrimes(20))