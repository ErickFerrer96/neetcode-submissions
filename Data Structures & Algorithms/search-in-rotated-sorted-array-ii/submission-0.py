class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo+hi)//2

            if nums[mid] == target:
                return True

            if nums[lo] == nums[mid] == nums[hi]:
                hi -= 1
                lo += 1
                continue

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid +1

            elif nums[hi] >= nums[mid]:
                if nums[hi] >= target > nums[mid]:
                    lo = mid + 1
    
                else:
                    hi = mid - 1

        return False
