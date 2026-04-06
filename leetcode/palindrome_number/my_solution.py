class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = []
        for i in str(x):
            a.append(i)
        b = a.copy()
        b.reverse()
        if a == b:
            return True
        else:
            return False

obj = Solution()
print(obj.isPalindrome(-121))