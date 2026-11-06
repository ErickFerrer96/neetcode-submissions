class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index1 = 0

        while index1 < len(nums)-1:

            index2 = index1+1
            
            while index2 <= len(nums)-1:
                
                if nums[index1] == nums[index2]:
                    if (index2-index1) <= k:
                        return True
                if (index2-index1) > k:
                    break
        
                index2 += 1

            index1 += 1

        return False
