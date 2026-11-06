class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        Counter = majorElement = 0

        for num in numSet:
            if Counter < nums.count(num):
                Counter = nums.count(num)
                majorElement = num
    
        return majorElement