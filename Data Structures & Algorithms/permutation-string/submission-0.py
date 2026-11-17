class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        auxDic = {}

        for letter in s1:
            if letter in auxDic:
                auxDic[letter] += 1
            else:
                auxDic[letter] = 1

        for r in range(len(s2)):
            if s2[r] not in auxDic:
                auxDic[s2[r]] = -1
            else:
                auxDic[s2[r]] -= 1
            
            if r >= len(s1) :
                auxDic[s2[r - len(s1)]] += 1
                
            if all(value == 0 for value in auxDic.values()):
                return True
            
        
        return False
        