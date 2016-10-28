class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result=0
        for i in s:
            result^=1<<(ord(i)-ord("a"))
        for i in t:
            result^=1<<(ord(i)-ord("a"))
        number=0
        print (result)
        for i in range(5):
            result>>1
            print(result)
        return chr(ord("a")+number)
if __name__ =="__main__":
    print(Solution().findTheDifference("abcd","abcde"))