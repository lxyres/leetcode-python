
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        number=[]
        now=0
        for i in s:
            if i=="+":
                now+=1
            else:
                if now>1:
                    number.append(now)
                    now=0
                else:
                    now=0
        if now>1:
            number.append(now)
        if not number:
            return False
        n=max(number)
        print(number)
        table=[0,0,1,1]
        for i in range(4,n+1):
            nums=[]
            for j in range((i+1)//2):
                nums.append(table[j]^table[i-j-2])
            table.append(self.firstMissingPositive(nums))
        result=0
        print(table)
        for i in number:
            result^=table[i]
        if result==0:
            return False
        else:
            return True
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        index=0
        n=len(nums)
        while index<n:
            if nums[index]>= 0 and nums[index]<n and nums[index]!=index and nums[nums[index]]!=nums[index]:
                nums[nums[index]],nums[index]=nums[index],nums[nums[index]]
            else:
                index+=1
        for i,v in enumerate(nums):
            if i!=v:
                return i
        return n
if __name__ =="__main__":
    print(Solution().canWin("+-+--+++--++"))