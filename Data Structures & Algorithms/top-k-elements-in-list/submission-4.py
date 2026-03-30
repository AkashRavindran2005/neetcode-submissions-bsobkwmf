class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        freq = [[] for i in range(len(nums)+1)]
        for num, cnt in d.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                if j not in res:
                    res.append(j)
                    if len(res) == k:
                        return res