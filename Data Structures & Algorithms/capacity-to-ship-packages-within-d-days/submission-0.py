class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        hi = sum(weights)
        lo = max(weights)

        while lo <= hi:
            mid = (lo+hi)//2
            charge = 0
            dayCounter = 1

            for weight in weights:
                if charge + weight <= mid:
                    charge += weight
                else:
                    charge = weight
                    dayCounter += 1


            if dayCounter <= days:
                response = mid
                hi = mid - 1
            else:
                lo = mid +1
        
        return response


        