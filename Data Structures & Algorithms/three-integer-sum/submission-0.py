class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsorted = sorted(nums)
        result = []
        for i in range(len(numsorted)):
            if i > 0 and numsorted[i] == numsorted[i-1]:
                continue
            l = i +1
            r = len(numsorted)-1
            while l < r:
                threesum = numsorted[i] + numsorted[l] + numsorted[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    result.append([numsorted[i], numsorted[l], numsorted[r]])
                    l += 1
                    r -= 1
                    while numsorted[l] == numsorted[l-1] and l < r:
                        l += 1
        return result
