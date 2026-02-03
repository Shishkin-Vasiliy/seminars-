class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def rotateRight(self, head, k):
#         n = len(head)
#         K = k % n

#         lead = ListNode(head[0], None) # создание первого узла
#         current = lead                 # создание указателя на него

#         for i in range(1, n):               # создание указателей next для всего списка, последний указывает на None
#             current.next = ListNode(head[i])
#             current = current.next
#         current.next = lead # после выполнения цикла current это последний элемент списка, значит ставим ему следующим указателем голову списка, тем самым замыкаем список в кольцо
 
#         for _ in range(n - K):
#             current = current.next # проходим n - K шагов (начиная с последнего элемента), чтобы попасть в элемент который будет новым хвостом, его следующим станет новая голова и в этот момент нужно разорвать между ними связь
#         new_lead = current.next    
#         current.next = None  
        
#         return new_lead
        
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        n = 1
        current = head
        if k == 0:
            return head
        
        while current.next:  #пока не None, проходим по списку и считаем длину n
            current = current.next
            n += 1            

        current.next = head

        
        K = k % n    

        for _ in range(n - K):  # теперь проходим n - K  раз по списку чтобы оказаться в новом хвосте, его next - новая голова списка, обозначаем это и рвем связь между хвостом и головой
            current = current.next
        new_head = current.next
        current.next = None

        return new_head    

        


            
            

