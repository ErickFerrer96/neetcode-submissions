class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        lowK = k%n

        self.reverse(nums,0,n-1)
        self.reverse(nums,0,lowK-1)
        self.reverse(nums,lowK,n-1)

        
    def reverse(self, nums, init, end):

        l = init
        r = end

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1


