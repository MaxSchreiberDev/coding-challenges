class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        for c, i in enumerate(strs[0]):
            l = []
            for a in strs:
                if len(a)-1 >= c and a[c] == i:
                    l.append(a[c])
                else:
                    l.append(False)
            if all(l):
                prefix += i
            else:
                break
        return prefix

# Ganz kurz, ich war extrem fucking close an der eigentlichen Lösung. 

obj = Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))
print("---")
print(obj.longestCommonPrefix(["ab", "a"]))