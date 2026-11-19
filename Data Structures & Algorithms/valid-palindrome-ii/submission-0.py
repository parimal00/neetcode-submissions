class Solution:
    def checkPalindrome(self, s, left, right):
        while left <= right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True

    def validPalindrome(self, s: str) -> bool:

        left=0
        right = len(s)-1
        count=0

        while left<=right:
            if s[left] != s[right]:
                leftCheck = self.checkPalindrome(s, left+1, right)
                rightCheck = self.checkPalindrome(s, left, right-1)
                return leftCheck or rightCheck
            
            left+=1
            right-=1

        return True