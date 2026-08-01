class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1
        arr = []
        for cnt, num in d.items():
            arr.append([num, cnt])
        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res