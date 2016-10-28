class MaxHeap:
    def __init__(self):
        self.heap=[[0,1]]
        self.size = 0
        self.dic={}
    def insert(self,number):
        #print(len(self.heap),self.size+1)
        if number in self.dic:
            self.heap[self.dic[number]][1]+=1
            return
        self.size+=1
        self.heap.append([number,1])
        self.dic[number]=self.size
        s2=self.size
        s1=s2//2
        while s1>0:
            if self.heap[s1][0]<self.heap[s2][0]:
                self.dic[self.heap[s1][0]],self.dic[self.heap[s2][0]]=s2,s1
                self.heap[s1],self.heap[s2]=self.heap[s2],self.heap[s1]
                s2=s1
                s1=s1//2
            else:
                break
    def pp(self):
        print(self.heap)
    def delete(self,number):
        #print(len(self.heap),self.size+1)
        if number not in self.dic:
            return
        if self.size==0:
            return
        idx=self.dic[number]
        if self.heap[idx][1]>1:
            self.heap[idx][1]-=1
        else:
            del self.dic[number]
            self.heap[idx]=self.heap[self.size]
            self.dic[self.heap[idx][0]]=idx
            self.heap.pop()
            self.size-=1
            while idx*2<=self.size:
                nidx=idx*2
                if nidx+1<=self.size and  self.heap[nidx+1][0]>self.heap[nidx][0]:
                    nidx+=1
                if self.heap[idx][0]<self.heap[nidx][0]:
                    self.dic[self.heap[idx][0]],self.dic[self.heap[nidx][0]]=nidx,idx
                    self.heap[idx],self.heap[nidx]=self.heap[nidx],self.heap[idx]
                    idx=nidx
                else:
                    break
    def maxLine(self):
        if self.size==0:
            return 0
        return self.heap[1][0]
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        line=[]
        for x in buildings:
            line.append([x[0],x[2]])
            line.append([x[1],-x[2]])
        line.sort(key=lambda x:(x[0],-x[1]))
        print(line)
        heap=MaxHeap()
        result=[]
        current=0
        for building in line:
            if building[1]>0:
                heap.insert(building[1])
            else:
                heap.delete(-building[1])
            print(current,heap.maxLine())
            heap.pp()
            if heap.maxLine()!=current:
                result.append([building[0],heap.maxLine()])
                current=heap.maxLine()
        return result
if __name__ =="__main__":
     print(Solution().getSkyline([[2190,661048,758784],[9349,881233,563276],[12407,630134,38165],[22681,726659,565517],[31035,590482,658874],[41079,901797,183267],[41966,103105,797412],[55007,801603,612368],[58392,212820,555654],[72911,127030,629492],[73343,141788,686181],[83528,142436,240383],[84774,599155,787928],[106461,451255,856478],[108312,994654,727797],[126206,273044,692346],[134022,376405,472351],[151396,993568,856873],[171466,493683,664744],[173068,901140,333376],[179498,667787,518146],[182589,973265,394689],[201756,900649,31050],[215635,818704,576840],[223320,282070,850252],[252616,974496,951489],[255654,640881,682979],[287063,366075,76163],[291126,900088,410078],[296928,373424,41902],[297159,357827,174187],[306338,779164,565403],[317547,979039,172892],[323095,698297,566611],[323195,622777,514005],[333003,335175,868871],[334996,734946,720348],[344417,952196,903592],[348009,977242,277615],[351747,930487,256666],[363240,475567,699704],[365620,755687,901569],[369650,650840,983693],[370927,621325,640913],[371945,419564,330008],[415109,890558,606676],[427304,782478,822160],[439482,509273,627966],[443909,914404,117924],[446741,853899,285878],[480389,658623,986748],[545123,873277,431801],[552469,730722,574235],[556895,568292,527243],[568368,728429,197654],[593412,760850,165709],[598238,706529,500991],[604335,921904,990205],[627682,871424,393992],[630315,802375,714014],[657552,782736,175905],[701356,827700,70697],[712097,737087,157624],[716678,889964,161559],[724790,945554,283638],[761604,840538,536707],[776181,932102,773239],[855055,983324,880344]]))