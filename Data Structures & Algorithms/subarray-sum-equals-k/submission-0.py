class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum={0:1}
        counter = total = 0
        
        for num in nums:
            total += num
            if total-k in prefix_sum:
                counter += prefix_sum[total - k]
            if total in prefix_sum:
                prefix_sum[total] += 1
            else:
                prefix_sum[total] = 1
        
        return counter
                
        