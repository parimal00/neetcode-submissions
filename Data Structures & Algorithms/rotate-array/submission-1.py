class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0]*len(nums)

        k %= len(nums)
        if k == 0:
            return

        index=(len(nums)-k)

        iterator = 0
        for i in range(index, len(temp)):
            temp[iterator]=nums[i]
            iterator+=1

        for i in range(index):
            print(i)
            temp[iterator]=nums[i]
            iterator+=1
        
        for i in range(len(nums)):
            nums[i] = temp[i]

        