class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        if len(nums)<4:
            return result
        save={}
        for i1,v1 in enumerate(nums):
            for i2,v2 in enumerate(nums[i1+1:]):
               if v1+v2 in save:
                   save[v1+v2].append([i1,i1+i2+1,v1,v2])
               else:
                   save[v1+v2]=[[i1,i1+i2+1,v1,v2]]
        for i1,v1 in enumerate(nums):
            for i2,v2 in enumerate(nums[i1+1:]):
                index=target-v1-v2
                print (i1,i2+i1+1,v1,v2)
                if index in save:
                    for i in save[index]:
                        if i2+i1+1<i[0]:
                            element=[v1,v2,i[2],i[3]]
                            element.sort()
                            result.append(element)
        return result
if __name__ == "__main__":
    print(Solution().fourSum([-3,-2,-1,0,0,1,2,3],0))