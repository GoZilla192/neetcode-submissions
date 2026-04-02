

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        from collections import Counter

        s_counter = Counter(s)
        t_counter = Counter(t)

        for char in t_counter:
            if t_counter[char] != s_counter[char]:
                return False

        return True
