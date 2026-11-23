class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        
        left=0
        min_window = float('inf')
        for i, n in enumerate(nums):
            sum+=n

            while sum >= target:
                window = i-left
                min_window=min(min_window, window+1)

                sum-=nums[left]
                left+=1
        
        if min_window == float('inf'):
            return 0

        return min_window

            


        