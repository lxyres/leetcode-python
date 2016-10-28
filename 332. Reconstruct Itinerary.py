class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        itineraries=[]
        table={}
        for ticket in tickets:
            if ticket[0]=="JFK":
                itineraries.append([ticket[1]])
            else:
                if ticket[0] in table:
                    table[ticket[0]].append(ticket[1])
                else:
                    table[ticket[0]]=[ticket[1]]
        print(table)
        for i in table:
            table[i].sort(reverse=True)
        print(table)
        print(itineraries)
        itineraries.sort(key=lambda x:x[0])
        print(itineraries)
        for i in itineraries:
            while i[-1] in table:
                j=table[i[-1]]
                if len(j)==1:
                    i.append(j[0])
                    del table[i[-2]]
                else:
                    i.append(j.pop())
            print(table)
        itineraries.sort(key= lambda x:(x[-1]!="JFK","".join(x)))
        result=["JFK"]
        for i in itineraries:
            result+=i
        return result
if __name__ =="__main__":
    print(Solution().findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]))