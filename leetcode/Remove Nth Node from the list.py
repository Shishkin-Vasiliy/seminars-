
from typing import Optional
from typing import List

head = [1,2,3,4,5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass
        l = []
        for i in range(len(head)):
            N = ListNode(head[i], i + 1).val
            l.append(N)
        index = len(head) - n 
        removed = l.pop(index)
        l[index - 1] = ListNode(head[index - 1], index + 1).val
        
        return l 

S = Solution()
print(S.removeNthFromEnd(head, 2))