class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if k<=0 or not nums1 or not nums2:
            return []
        result=[]
        """
        if k>=len(nums1)*len(nums2):
            for i in nums1:
                for j in nums2:
                    result.append([i,j])
            result.sort(key=lambda x:x[0]+x[1])
            return result
        """
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        table=[0 for i in range(len(nums1))]

        while k>0:
            tmp=None
            indexi=None
            indexj=None
            for i in range(len(nums1)):
                if tmp==None:
                    if table[i]<len(nums2):
                        tmp=nums1[i]+nums2[table[i]]
                        indexi=i
                        indexj=table[i]
                else:
                    if table[i]<indexj:
                        if nums1[i]+nums2[table[i]]<tmp:
                            tmp=nums1[i]+nums2[table[i]]
                            indexi=i
                            indexj=table[i]
                    else:
                        break
            print(result,tmp,k)
            if tmp==None:
                break
            else:
                result.append([nums1[indexi],nums2[indexj]])
                table[indexi]+=1
                k-=1
        return result
if __name__ =="__main__":
    print(Solution().kSmallestPairs([1,2,4],[-1,1,2],100))