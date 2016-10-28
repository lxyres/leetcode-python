class Solution(object):
    dic={'1':[],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
         '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z'],'0':['\t']}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result=[]
        if not digits:
            return result
        self.deepTraversal(digits,"",result)
        return result
    def deepTraversal(self, digits,former,result):
        if not digits:
            print("now",former)
            result.append(former)
            print(len(result))
            return
        print(len(self.dic[digits[0]]))
        for value in self.dic[digits[0]]:
            print((former+value))
            self.deepTraversal(digits[1:],former+value,result)
            
if __name__ == "__main__":
    print(Solution().letterCombinations('2'))