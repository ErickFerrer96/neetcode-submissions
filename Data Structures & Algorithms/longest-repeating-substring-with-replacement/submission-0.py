class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = record = 0
        auxDic = {}

        for r in range(len(s)):

            if s[r] in auxDic:
                auxDic[s[r]] += 1
            else:
                auxDic[s[r]] = 1

            while (r-l+1) - max(auxDic.values())> k:
                auxDic[s[l]] -= 1
                l += 1
            
            if (r - l+1) > record:
                record = r - l+1
        
        return record

          

        