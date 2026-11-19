class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        for char in s:
            hashmap[char] = hashmap.get(char,0) + 1

        for t_char in t:
            if hashmap.get(t_char) is None:
                return False
            
            hashmap[t_char] = hashmap[t_char] -1

        
        for i in hashmap:
            if hashmap[i] != 0:
                return False

        return True
        