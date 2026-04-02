class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        offset = ord('a')

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - offset] += 1
            
            anagrams[tuple(count)].append(string)

        return list(anagrams.values())