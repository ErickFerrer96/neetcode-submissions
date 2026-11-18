class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        totalSum = 0
        record = float('inf')

        for r in range(len(nums)):
            totalSum += nums[r]
            while totalSum >= target:
                record = min(record, r - l + 1)
                totalSum -= nums[l]
                l += 1

        if record == float('inf'):
            return 0
        else:
            return record               
