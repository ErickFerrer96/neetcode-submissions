class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0
        valueToSave = nums[0]

        for i in range(len(nums)):
            
            if valueToSave == nums[i]:
                continue

            else:
                valueToSave = nums[i]
                pos += 1
                nums[pos] = valueToSave

        return pos+1
                