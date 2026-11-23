class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_array = [0]*26
        s2_array=[0]*26

        for i in range(len(s1)):
            s1_array[ord(s1[i])-ord('a')]+=1
            s2_array[ord(s2[i])-ord('a')]+=1

        if s1_array == s2_array:
            return True

        left=0
        for i in range(len(s1), len(s2)):
            s2_array[ord(s2[i])-ord('a')]+=1
            s2_array[ord(s2[left])-ord('a')]-=1
            left+=1

            if s1_array == s2_array:
                return True

        return False



        
        
        