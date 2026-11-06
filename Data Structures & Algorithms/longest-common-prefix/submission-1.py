class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) < 2:
            return strs[0]
        
        Prefix = self.getPrefix(strs[0], strs[1])

        for i in range(len(strs)):
            if strs[i].startswith(Prefix):
                continue
            else:
                Prefix = self.getPrefix(strs[i-1], strs[i])
            if Prefix == "":
                break

        return Prefix


    def getPrefix(self, First, Second):

        prefix = ""

        minor = min(len(First), len(Second))

        for i in range(minor):
            if First[i] != Second[i]:
                break
            else:
                prefix += First[i]

        return prefix
        