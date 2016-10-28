class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        s1=0
        s2=len(s)-1
        while s1<s2:
            if s[s1] not in vowels:
                s1+=1
            else:
                break
        while s1<s2:
            if s[s2] not in vowels:
                s2-=1
            else:
                break
        while s1<s2:
            s=s[:s1]+s[s2]+s[s1+1:s2]+s[s1]+s[s2+1:]
            s1+=1
            s2-=1
            while s1<s2:
                if s[s1] not in vowels:
                    s1+=1
                else:
                    break
            while s1<s2:
                if s[s2] not in vowels:
                    s2-=1
                else:
                    break
        return s
if __name__ == "__main__":
    print(Solution().reverseVowels("hello"))