class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()          # 1. Whitespace entfernen
        if not s:
            return 0
        
        sign = 1                # 2. Vorzeichen
        i = 0
        if s[0] in "+-":
            if s[0] == "-":
                sign = -1
            i = 1
        
        awn = 0
        while i < len(s) and s[i].isdigit():   # 3. Ziffern lesen
            awn = awn * 10 + int(s[i])
            i += 1
        
        awn *= sign             # 4. Vorzeichen anwenden
        
        awn = max(-2**31, min(2**31 - 1, awn))  # 5. Clamping
        return awn

obj = Solution()
print(obj.myAtoi(" +-42"))