class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def counttable(table):
            for i in range(10):
                for j in range(10):
                    table[(str(i),str(j),"0")]=[str((i+j)%10),str((i+j)//10)]
                    table[(str(i),str(j),"1")]=[str((i+j+1)%10),str((i+j+1)//10)]
            return
        def countdic(num2,table,dic):
            dic["0"]=""
            dic["1"]=num2
            for i in range(2,10):
                dic[str(i)]=add(dic[str(i-1)],num2)
        def add(s1,s2):
            last="0"
            result=""
            if len(s1)>len(s2):
                for i in range(len(s2)):
                    tmp=table[(s1[i],s2[i],last)]
                    result+=(tmp[0])
                    last=tmp[1]
                for i in range(len(s2),len(s1)):
                    tmp=table[(s1[i],'0',last)]
                    result+=tmp[0]
                    last=tmp[1]
                result+=(last)
            else:
                for i in range(len(s1)):
                    tmp=table[(s1[i],s2[i],last)]
                    result+=(tmp[0])
                    last=tmp[1]
                for i in range(len(s1),len(s2)):
                    tmp=table[(s2[i],'0',last)]
                    result+=tmp[0]
                    last=tmp[1]
                result+=last
            result=result.rstrip("0")
            return result
        num1=num1[::-1]
        num2=num2[::-1]
        result="0"
        table={}
        counttable(table)
        dic={}
        countdic(num2,table,dic)
        print(table)
        print(dic)
        for i,v in enumerate(num1):
            result=add(result,"0"*i+dic[v])
        if result=="":
            return '0'
        result=result[::-1]
        return result
if __name__ == "__main__":
    print(Solution().multiply("0","0"))