class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count =0
        phead = head
        if(n<=0):
            return None
        while(phead != None):
            count +=1
            phead=phead.next
        if(count<n):
            return None
        if(count == n):
            return head.next
        d = count - n
        Node_temp1 = []
        phead = head
        while(d>0):
            if (d == 1):
                Node_temp1 = phead
            phead = phead.next
            d -= 1
        Node_temp1.next = phead.next

        return head

head1 = ListNode(1)
head2 = ListNode(2)
head3 = ListNode(3)
head1.next = head2
head2.next = head3
n = 3
res = Solution().removeNthFromEnd(head1,n)
while(res != None):
    print(res.val)
    res = res.next