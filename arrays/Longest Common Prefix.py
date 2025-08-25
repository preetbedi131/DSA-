"""Input: strs = ["flower","flow","flight"]
Output: "fl""""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=""
        for i in range(len(strs[0])):
            char=strs[0][i]
            for words in strs[1:]:
                if i>=len(words) or char!=words[i]:
                    return prefix
            prefix +=char
        return prefix
