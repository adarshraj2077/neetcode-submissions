class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i<j:
            if s[i].isalnum() != s[j].isalnum():
                return True
            else:
                return False