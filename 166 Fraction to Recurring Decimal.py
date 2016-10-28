class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        zheng=0
        while numerator>=denominator:
            zheng+=1
            numerator-=1
        yu=""
        store={}
        now=0
        while numerator!=0:
            print (numerator)
            if numerator in store:
                tmp=store[numerator]
                return str(zheng)+"."+yu[:tmp]+"("+yu[tmp:]+")"
            else:
                tmp=numerator*10
                yu+=str(tmp//denominator)
                store[numerator]=now
                now+=1
                numerator=tmp%denominator
        return str(zheng)+"."+yu
if __name__=="__main__":
    print(Solution().fractionToDecimal(1,6))