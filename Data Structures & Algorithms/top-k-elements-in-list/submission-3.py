class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        freq = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        for num, cnt in d.items():
            freq[cnt].append(num)
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                l.append(num)
                if len(l) == k:
                    return l