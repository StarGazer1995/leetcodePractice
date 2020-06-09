class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class solution:
    def copyList(self,node):
        pHead1 = node
        while(pHead1):
            pHead2 = Node(pHead1.val)
            pHead2.next = pHead1.next
            pHead1.next = pHead2
            pHead1 = pHead2.next
        return node

    def linkList(self,node:'Node'):
        pHead1 = node
        pHead2 = node.next
        while(pHead2):
            pHead2.random = pHead1.random.next
            pHead1 = pHead1.next.next
            if not pHead2.next:
                pHead2 = pHead2.next
            else:
                pHead2 = pHead2.next.next
        return node
    def devideList(self,node):
        pHead1 = node
        pHead2 = node.next
        ans = pHead2
        while(pHead2 and pHead2.next):
            pHead1.next = pHead1.next.next
            pHead2.next = pHead2.next.next
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return ans
    def  CopyListwithRandomPointer(self,node):
        ans = self.copyList(node)
        ans = self.linkList(ans)
        ans = self.devideList(ans)
        return ans

ans = Node(0)
head = ans
for i in range(1,5):
    ans.next = Node(i)
    ans = ans.next
ans = head
while(ans):
    ans.random = head
    ans = ans.next
ans = head

ans2 = solution().CopyListwithRandomPointer(head)
while(ans2):
    print(ans2.val,ans2.random.val)
    ans2 = ans2.next;