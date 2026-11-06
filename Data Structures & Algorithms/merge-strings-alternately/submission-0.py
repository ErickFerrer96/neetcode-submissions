class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newString = ""
        index1 = 0
        index2 = 0

        while index1 < len(word1) and index2 < len(word2):
            newString += word1[index1]
            newString += word2[index2]

            index1 += 1
            index2 += 1

        if index1 == len(word1) and index2 != len(word2):
            newString += word2[index2:]
        else:
            newString += word1[index1:]

        return newString 

