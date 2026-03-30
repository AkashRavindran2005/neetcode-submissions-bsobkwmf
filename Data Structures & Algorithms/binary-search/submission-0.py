class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0
        while low < high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid
            if nums[mid] < target:
                low = mid
            else:
                return -1
        