nums = list(map(int, input().split()))
def RemoveDuplicates(nums):
    if not nums:
        return 0, None
    s, f = 0, 1
    while f < len(nums):
        if nums[s] == nums[f]:
            f += 1
        else:
            nums[s + 1] = nums[f]
            s += 1
            f += 1
    return s + 1, nums 
print(RemoveDuplicates(nums))


      