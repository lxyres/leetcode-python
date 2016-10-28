class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        xmin=min([i[0] for i in rectangles])
        xmax=max([i[2] for i in rectangles])
        ymin=min([i[1] for i in rectangles])
        ymax=max([i[3] for i in rectangles])
        de={}
        for rec in rectangles:
            for i in range(rec[0],rec[2]):
                for j in range(rec[1],rec[3]):
                    if i in de:
                        if j in de[i]:
                            de[i][j]+=1
                        else:
                            de[i][j]=1
                    else:
                        de[i]={}
                        de[i][j]=1
        defa=None
        print(de)
        if xmin in de:
            if ymin in de[xmin]:
                defa=de[xmin][ymin]
            else:
                return False
        else:
            return False
        for i in range(xmin,xmax):
            for j in range(ymin,ymax):
                if i in de:
                    if j in de[i]:
                        if de[i][j]!=defa:
                            return False
                    else:
                        return False
                else:
                    return False
        return True
if __name__ =="__main__":
     print(Solution().isRectangleCover([[0,0,4,1],[0,0,4,1]]))