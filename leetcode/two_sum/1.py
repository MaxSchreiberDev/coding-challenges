class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for d in range(len(nums)):
                if nums[i] + nums[d] == target and not i == d:
                    return [i,d]

obj = Solution()
print(obj.twoSum([2,7,11,15], 9))