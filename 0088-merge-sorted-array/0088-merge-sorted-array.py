class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) > m:
            nums1.pop()
        
        while n > 0:
            nums1.append(nums2[n-1])
            n-=1
        nums1.sort()
        
        