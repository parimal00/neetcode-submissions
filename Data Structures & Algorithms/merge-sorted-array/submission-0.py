class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        left = m-1
        right = n-1
        index = m + n -1
        iteration = 0
        while right >= 0:
            if left >=0 and nums1[left] > nums2[right]:
                nums1[index] = nums1[left]
                left-=1
            else:
                nums1[index] = nums2[right]
                right-=1

            index=index-1
            iteration-=1

        