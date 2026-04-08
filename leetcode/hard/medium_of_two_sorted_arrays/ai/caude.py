class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1 += nums2
        
        nums1.sort()
        
        mid = len(nums1) // 2
        if len(nums1) % 2 == 0:
            return (nums1[mid - 1] + nums1[mid]) / 2
        else:
            return float(nums1[mid])

obj = Solution()
print(obj.findMedianSortedArrays([1,3], [2]))