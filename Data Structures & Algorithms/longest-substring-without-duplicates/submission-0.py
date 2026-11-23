class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap={}
        left=0
        max_length=0

        for right, n in enumerate(s):
            if hashmap.get(n) is not None:
                left=max(left, hashmap[n] +1)

            hashmap[n] = right
            
            length = (right-left+1)
            max_length=max(max_length, length)

        return max_length
        