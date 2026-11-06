class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        val = len(nums)/3
        auxDic  = {}
        auxList = []

        for num in nums:
            if num in auxDic:
                auxDic[num] += 1
            else:
                auxDic[num] = 1
        
        for key, count in auxDic.items():
            if count > val:
                auxList.append(key)

        return auxList
        