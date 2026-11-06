class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Result = []

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    Result.append(i)
                    Result.append(j)
                    return Result

        return 0        

        