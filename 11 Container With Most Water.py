class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        last=height[0]
        stack=[[0,height[0]]]
        contain=0
        for index,value in enumerate(height[1:]):
            if value<last:
                stack.append([index,value])
                contain+=value
                last=value
            else:
                contain+=last
                while stack :
                    i,v=stack.pop()
                    if v>value:
                        contain+=(index-i)*(value-last)
                        stack.append([i,v])
                        break
                    else:
                        contain+=(index-i)*(v-last)
                        last=v
                last=value
        return contain
