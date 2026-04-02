class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_chars = [0] * 26
        balance = 0
        offset = ord('a')

        for char in s:
            count_chars[ord(char) - offset] += 1
    
        for char in t:
            idx = ord(char) - offset
            count_chars[idx] -= 1

            if count_chars[idx] < 0:
                return False
        
        return sum(count_chars) == 0
