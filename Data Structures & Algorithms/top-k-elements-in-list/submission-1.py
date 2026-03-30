class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        if len(nums) <= k:
            return nums
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            if d[nums[i]] >= k:
                l.append(nums[i])
            d[nums[i]] += 1
        return list(set(l))