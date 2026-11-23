class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        sorted_s1 = "".join(sorted(s1))

        left=0
        for i in range(len(s1)-1, len(s2)):
            substring = s2[left: i+1]
            print(substring)

            sorted_substring = "".join(sorted(substring))

            if sorted_s1 == sorted_substring:
                return True
            
            left+=1

        return False



        
        
        