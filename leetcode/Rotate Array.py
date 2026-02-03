A = list(map(int, input().split()))
n = len(A)
k = int(input())
K = k % n

# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

# class Solution:
#     def CycleShift(self, A):
#         l = []
#         for i in range(n):
#             l[i].next = l[i + 1]
#         return l    

# S = Solution()
# print(S.CycleShift(A))                

left = 0
right = n - 1
while left < right:
    A[left], A[right] = A[right], A[left]
    left += 1
    right -= 1

left = 0
right = K - 1
while left < right:
    A[left], A[right] = A[right], A[left]
    left += 1
    right -= 1

left = K
right = n - 1
while left < right:
    A[left], A[right] = A[right], A[left]
    left += 1
    right -= 1

print(A)    