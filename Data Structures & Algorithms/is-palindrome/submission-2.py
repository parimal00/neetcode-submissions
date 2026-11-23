class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join(s.split(" "))

        left=0
        right = len(s) -1
        s=s.lower()
        while left < right:
            while left<right and  (s[left] == " " or not s[left].isalnum()):
                left+=1

            while left<right and (s[right] == " " or not s[right].isalnum()):
                right-=1
            
            if s[left] != s[right]:
                return False
            
            left+=1
            right-=1

        return True