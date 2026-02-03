from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return nums[0]
        triples = []
        Nums = sorted(nums)
                                         #сортируем массив, далее выбираем первый элемент тройки, берем часть массива больше него, 1 указатель - второй элемент, 2 указатель - третий элемент, в зависимости от знака их суммы двигаем указатели и заносим в список
        for i in range(n - 2):
            if i > 0 and Nums[i] == Nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while r > l:
                sum = Nums[i] + Nums[l] + Nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    triples.append([Nums[i], Nums[l], Nums[r]])
                    l += 1
                    r -= 1
                    while l < r and Nums[l] == Nums[l - 1]:
                        l += 1
                    while l < r and Nums[r] == Nums[r + 1]:
                        r -= 1
                        
        return triples            


solution = Solution()
result = solution.threeSum([-1, -1, 2, -1, -1, -1, 2, 2])
print(result)  


