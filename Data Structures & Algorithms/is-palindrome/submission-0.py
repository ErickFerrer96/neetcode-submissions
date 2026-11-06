class Solution:
    def isPalindrome(self, s: str) -> bool:

        print(s[::-1])

        cleanS = ""

        for letter in s:
            if letter.isalnum():
                cleanS += letter.lower()

        if cleanS == cleanS[::-1]:
            return True

        return False
        