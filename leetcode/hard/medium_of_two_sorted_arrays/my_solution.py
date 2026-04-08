# Import statistics Library
import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        for i in nums2:
            nums1.append(i)
        
        print(nums1)
        return statistics.median(sorted(nums1))

obj = Solution()
print(obj.findMedianSortedArrays([2,2,4,4], [2,2,2,4,4]))