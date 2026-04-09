class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        counter = 0
        l = nums
        while True:
            if len(l) == 1:
                if l[0]>=target:
                    break
                else:
                    counter += 1
                    break
            
            c = len(l)//2
            print("L: ", l, " Target: ", target, " C: ", c)
            
            if l[c] >= target:
                l = l[:c]
            elif l[c] <= target:
                l = l[c:]
                counter += int(len(l[:c]))
        return counter

obj = Solution()
print("---")
print("TEST 1: nums = [1,3,5,6], target = 0")
print(obj.searchInsert([1,3,5,6], 0))
print("---")
print("TEST 2: nums = [1,3,5,6], target = 7")
print(obj.searchInsert([1,3,5,6], 7))
print("---")
print("TEST 3: nums = [1], target = 0")
print(obj.searchInsert([1], 0))