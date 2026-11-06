class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleanS = ""

        for letter in s:
            if letter.isalnum():
                cleanS += letter.lower()

        if cleanS == cleanS[::-1]:
            return True

        return False
        