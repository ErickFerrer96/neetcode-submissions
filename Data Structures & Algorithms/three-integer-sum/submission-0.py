class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        auxNums = sorted(nums)
        result = []

        for idx in range(len(auxNums)):
            left = idx + 1
            right = len(auxNums) -1

            if auxNums[idx] > 0: 
                break
            if idx > 0 and auxNums[idx] == auxNums[idx - 1]:
                continue
            
            while left < right:
                resultSum = auxNums[idx] + auxNums[left] + auxNums[right]
                if resultSum == 0:
                    result.append([auxNums[idx],auxNums[left],auxNums[right]])
                    left += 1
                    right -= 1

                    while left < right and auxNums[left] == auxNums[left-1]:
                        left+=1

                elif resultSum > 0:
                    right -= 1
                elif resultSum < 0:
                    left += 1

        return result 