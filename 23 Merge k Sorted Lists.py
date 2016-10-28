# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        return self.mergeK(lists)
    def mergeK(self,lists):
        if len(lists)==1:
            return lists[0]
        index=len(lists)//2
        s1=mergeK(lists[:index])
        s2=mergeK(lists[index:])
        root=ListNode(0)
        tmp=root
        while(s1 and s2):
            if s1.val<s2.val:
                tmp.next=s1
                s1=s1.next
                tmp=tmp.next
            else:
                tmp.next=s2
                s2=s2.next
                tmp=tmp.next
        if not s1:
            tmp.next=s2
        else:
            tmp.next=s1
        return root.next