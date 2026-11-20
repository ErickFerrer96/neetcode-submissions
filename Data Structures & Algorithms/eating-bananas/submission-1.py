class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        response = hi = max(piles)

        while lo <= hi:
            mid = (lo+hi)//2
            hours = 0
            for pile in piles:
                hours += -(-pile//mid)
            
            print(hours)
            
            if hours <= h:
                response = mid
                hi = mid - 1
            else:
                lo = mid +1
        

        return response
        