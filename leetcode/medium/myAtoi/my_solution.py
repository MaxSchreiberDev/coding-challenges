class Solution:
    def myAtoi(self, s: str) -> int:
        awn = "0"
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        pre = ["+", "-"]
        specials = [" "]
        prefix = True
        negative = False
        for i in s:
            if i in numbers:
                awn += i
                prefix = False
            elif i in pre and prefix:
                if i == "-":
                    negative = True
                prefix = False
            elif i in specials: pass
            else: break
        if int(awn) > 2147483648:
            awn = 2147483648
            if negative:
                awn += 1
        if negative: return int(awn)*-1
        return int(awn)


obj = Solution()
print(obj.myAtoi(" +-42"))