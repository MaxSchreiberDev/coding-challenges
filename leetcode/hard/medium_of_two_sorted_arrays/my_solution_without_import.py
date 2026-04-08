class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        for i in nums2:
            nums1.append(i)
        
        nums1.sort()

        if len(nums1) % 2 == 0:
            c1,c2 = int(len(nums1) / 2 - 0.5),int(len(nums1) / 2 + 0.5)
            v1,v2 = nums1[c1],nums1[c2]
            return((v1 + v2) / 2)
        else:
            c = int(len(nums1) / 2 - 0.5) 
            return(nums1[c])

obj = Solution()
print(obj.findMedianSortedArrays([1,3], [2]))