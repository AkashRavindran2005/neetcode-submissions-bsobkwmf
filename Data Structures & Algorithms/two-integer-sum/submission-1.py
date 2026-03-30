class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i
            if target-nums[i] in seen and seen[target-nums[i]] != i:
                return [seen[target-nums[i]], i]