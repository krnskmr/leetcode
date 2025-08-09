class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        res = 0
        l = 0
        for i in range(len(s)):

            while s[i] in result:  #cuz we need to remove until all before elemnts get removed
                result.remove(s[l])
                l += 1
            result.add(s[i])
            res = max(res , i - l+1)
        return res
                
