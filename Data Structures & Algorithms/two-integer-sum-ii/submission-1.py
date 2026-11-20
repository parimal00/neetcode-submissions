class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}

        for i, n in enumerate(numbers):
            find = target-n

            if find in hashmap:
                return [hashmap[find]+1, i+1]
            
            hashmap[n]=i