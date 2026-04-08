class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:    
        seen = set()  # aktuell im Fenster
        left = 0      # linke Fenstergrenze
        max_len = 0

        for right in range(len(s)):        # rechte Grenze wächst immer
            while s[right] in seen:        # Duplikat gefunden?
                seen.remove(s[left])       # linke Seite rauswerfen
                left += 1                  # Fenster von links verkleinern
            seen.add(s[right])             # neues Zeichen ins Fenster
            max_len = max(max_len, right - left + 1)  # Fenstergröße messen

        return max_len

obj = Solution()
print(obj.lengthOfLongestSubstring("abcdefghijkla"))