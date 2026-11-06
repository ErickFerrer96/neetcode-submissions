class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        NotRepeat = [s[0]]
        for char in s[1:]:
            if char != NotRepeat[-1]:
                NotRepeat.append(char)

        for letter in NotRepeat: 
            if s.count(letter) != t.count(letter):
                return False
        
        return True

    
        