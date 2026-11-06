class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        auxDic = {}

        for word in strs:
            auxKey = sorted(word)
            auxKey = "".join(auxKey)

            if auxKey in auxDic:
                auxDic[auxKey].append(word)
            
            else:
                auxDic[auxKey] = []
                auxDic[auxKey].append(word)
        
        return list(auxDic.values())
        

                