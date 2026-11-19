class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap={}

        average = len(nums)/3

        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        
        results =[]
        for h in hashmap:
            if hashmap[h] > average:
                results.append(h)

        return results