class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxConsecutive = 0
        auxSet = set(nums)

        for num in auxSet:

            if num-1 not in auxSet:

                counter = 1

                while num+counter in auxSet:
                        counter += 1

                if counter > maxConsecutive:
                    maxConsecutive = counter
        
        return maxConsecutive


        