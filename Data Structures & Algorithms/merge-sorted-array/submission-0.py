class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lastPlace = len(nums1)-1
        index1 = m -1
        index2 = n -1
        
        while index1 >= 0 and index2 >= 0:

            if nums2[index2] > nums1[index1]:
                nums1[lastPlace] = nums2[index2]
                index2 -= 1
                lastPlace -= 1
            
            elif nums1[index1] > nums2[index2]:
                nums1[lastPlace] = nums1[index1]
                index1 -= 1
                lastPlace -= 1

            else:
                nums1[lastPlace] = nums2[index2]
                index2 -= 1
                lastPlace -= 1
        
        if index2 == -1:
            return 
        
        else: 

            while index2 >= 0:
                nums1[lastPlace] = nums2[index2]
                index2 -= 1
                lastPlace -= 1
            
            return
                