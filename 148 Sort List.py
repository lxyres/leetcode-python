class ListNode(object):
    def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        return self._sortList(head)[0]
    def _sortList(self,head):
        cout(head)
        if not head:
            return [None,None]
        s1=ListNode(0)
        tmp1=s1
        s2=ListNode(0)
        tmp2=s2
        tmp=head.next
        head_end=head
        while tmp:
            if tmp.val<head.val:
                tmp1.next=tmp
                tmp1=tmp1.next
            elif tmp.val==head.val:
                head_end.next=tmp
                head_end=head_end.next
            else:
                tmp2.next=tmp
                tmp2=tmp2.next
            tmp=tmp.next
        tmp1.next=None
        tmp2.next=None
        head_end.next=None
        left=self._sortList(s1.next)
        right=self._sortList(s2.next)
        if left[0]==None:
            s1=head
        else:
            left[-1].next=head
            s1=left[0]
        if right[0]==None:
            s2=head_end
        else:
            head_end.next=right[0]
            s2=right[-1]
        return [s1,s2]
def cout(head):
    while head:
        print(head.val)
        head=head.next
    print("end")
if __name__=="__main__":
    head=ListNode(2)
    head.next=ListNode(3)
    head.next.next=ListNode(4)
    head=Solution().sortList(head)
    cout(head)