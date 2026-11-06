class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        index1=0
        index2=len(s)-1
        
        while index1 < index2:
            AuxValue = s[index1]

            s[index1] = s[index2]
            s[index2] = AuxValue

            index2 -= 1
            index1 += 1
