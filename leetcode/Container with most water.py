# height = list(map(int, input().split()))
# n = len(height)

# left = 0
# right = n - 1
# S = []
# while right > left:
#     s = (right - left) * min(height[right], height[left])

#     if height[right] > height[left]:
#         left += 1
#     else:
#         right -= 1

#     S.append(s)    



# res = max(S)
# print(res)        

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0
        
        left, right = 0, n - 1
        max_area = 0
        
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area        

