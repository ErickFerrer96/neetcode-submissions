class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = record = 0
        auxSet = set()

        for r in range(len(s)):
            while s[r] in auxSet:
                auxSet.remove(s[l])
                l += 1
            auxSet.add(s[r])
            if (r - l+1) > record:
                record = r - l+1

        return record
