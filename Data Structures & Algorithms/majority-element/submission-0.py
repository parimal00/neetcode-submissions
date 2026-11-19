class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        for n in nums:
            hashmap[n] = hashmap.get(n,0) +1
        
        max_ele = 0
        data=None
        for h in hashmap:
            if hashmap[h] > max_ele:
                max_ele=hashmap[h]
                data=h

        
        return data


        