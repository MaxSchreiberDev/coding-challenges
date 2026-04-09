class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        for c, i in enumerate(strs[0]):
            if all(len(a) > c and a[c] == i for a in strs):
                prefix += i
            else:
                break
        return prefix

obj = Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))
print("---")
print(obj.longestCommonPrefix(["ab", "a"]))
print("---")
print(obj.longestCommonPrefix(["aaa", "aa", "aaa"]))