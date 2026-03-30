class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0 for i in range(len(nums))]
        prod, zero = 1, 0
        for i in nums:
            if i != 0:
                prod *= i
            else:
                zero += 1
        if zero > 1: return [0 for i in range(len(nums))]
        if zero > 0: return [prod if nums[i] == 0 else 0 for i in range(len(nums))]
        for i in range(len(nums)):
            l[i] = prod//nums[i]
        return l
            