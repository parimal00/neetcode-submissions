class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}

        left = 0
        for right, n in enumerate(nums):
            if (right-left) >k:
                element = nums[left]

                del hashmap[element]

                left+=1

            if hashmap.get(n) is not None:
                return True
            
            hashmap[n]=True

        
        return False



            
        