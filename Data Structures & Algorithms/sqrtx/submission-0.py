class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left <= right:
            mid = (right+left)//2

            sqr = mid*mid

            if sqr == x:
                return mid

            if sqr > x:
                right = mid-1
            
            if sqr < x:
                left = mid+1
                
        
        return right