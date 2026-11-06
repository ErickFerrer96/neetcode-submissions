class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        auxDic = {}

        for num in nums:
            if num in auxDic:
                auxDic[num] += 1
            else:
                auxDic[num] = 1
        
        orderAuxDic = sorted(auxDic, key=auxDic.get, reverse=True)

        return orderAuxDic[:k]
        