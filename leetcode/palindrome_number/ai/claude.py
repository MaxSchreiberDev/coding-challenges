class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

obj = Solution()
print(obj.isPalindrome(-121))