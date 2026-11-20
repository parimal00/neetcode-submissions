class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        hashmap={}

        for i, n in enumerate(nums):
            if n not in hashmap:
                nums[k] = nums[i]
                k=k+1
            
            hashmap[n]= True
        return k