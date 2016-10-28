class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n<1:
            return []
        if n==1:
            return ['()']
        s1=set()
        s1.add('()')
        for i in range(n-1):
            s2=set()
            for i in s1:
                s2.add('('+i+')')
            for i in s1:
                s2.add('()'+i)
            for i in s1:
                s2.add(i+'()')
            s1.clear()
            s1=s2
            print(s1)
        return [i for i in s1]

if __name__ == "__main__":
    print(Solution().generateParenthesis(3))