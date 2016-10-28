class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n=len(s)
        if n<4 or n>12:
            print('??')
            return []
        result =[]
        self.Ip1(s,result)
        return result
    def Ip1(self,s,result):
        if ord(s[0])==48:
            self.Ip2(s[0:1]+'.',s[1:],result)
        else:
            self.Ip2(s[0:1]+'.',s[1:],result)
            self.Ip2(s[0:2]+'.',s[2:],result)
            number=(ord(s[0])-48)*100+(ord(s[1])-48)*10+(ord(s[2])-48)
            if number<256:
                self.Ip2(s[0:3]+'.',s[3:],result)
    def Ip2(self,former,s,result):
        print("IP2",s)
        if len(s)<3:
            return
        if ord(s[0])==48:
            self.Ip3(former+s[0:1]+'.',s[1:],result)
        else:
            self.Ip3(former+s[0:1]+'.',s[1:],result)
            self.Ip3(former+s[0:2]+'.',s[2:],result)
            number=(ord(s[0])-48)*100+(ord(s[1])-48)*10+(ord(s[2])-48)
            if number<256:
                self.Ip3(former+s[0:3]+'.',s[3:],result)
    def Ip3(self,former,s,result):
        print("IP3",s)
        if len(s)<2:
            return
        if ord(s[0])==48:
            self.Ip4(former+s[0:1]+'.',s[1:],result)
        else:
            self.Ip4(former+s[0:1]+'.',s[1:],result)
            self.Ip4(former+s[0:2]+'.',s[2:],result)
            if len(s)==3:
                number=(ord(s[0])-48)*100+(ord(s[1])-48)*10+(ord(s[2])-48)
                if number<256:
                    self.Ip4(former+s[0:3]+'.',s[3:],result)
    def Ip4(self,former,s,result):
        print("IP4",s)
        n=len(s)
        if n<1 or n>3:
            return
        if n==1:
            result.append(former+s[0:])
        elif n==2:
            if ord(s[0])!=48:
                result.append(former+s[0:])
        else:
            number=(ord(s[0])-48)*100+(ord(s[1])-48)*10+(ord(s[2])-48)
            if number<256 and number>99:
                    result.append(former+s[0:])
if __name__ == "__main__":
    print(Solution().restoreIpAddresses("1111"))