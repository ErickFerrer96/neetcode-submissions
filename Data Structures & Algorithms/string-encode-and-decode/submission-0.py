class Solution:

    def encode(self, strs: List[str]) -> str:

        auxList = []

        for word in strs:
            size = len(word)
            auxList.append(str(size)+"#"+word)

        return "".join(auxList)

    def decode(self, s: str) -> List[str]:

        auxList = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            auxSize = int(s[i:j])

            auxList.append(str(s[j+1:j+auxSize+1]))

            i = auxSize+j+1
        
        return auxList

