class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = 0
        l = []
        for i, j in enumerate(s):
            l1 = []
            for a, b in enumerate(s):
                if a >= i:
                    if b not in l1:
                        l1.append(b)
                    else:
                        break
            l.append(l1)
                            
            for i in l:
                if len(i) > c:
                    c = len(i)
                    if c >= 95:
                        return c
                else:
                    l.remove(i)
                    print(l)

        return c



obj = Solution()
print(obj.lengthOfLongestSubstring("abcdefghijkla"))