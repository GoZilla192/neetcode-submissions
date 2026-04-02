class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i, char in enumerate(strs[0]):
            for string in strs:
                if i >= len(string) or char != string[i]:
                    return result
            
            result += char
        
        return result