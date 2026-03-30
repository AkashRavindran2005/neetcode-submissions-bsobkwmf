class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        result = 0
        l = 0
        maxf = 0
        for i in range(len(s)):
            mp[s[i]] = 1 + mp.get(s[i], 0)
            maxf = max(maxf, mp[s[i]])
            while (i - l + 1) - maxf > k:
                mp[s[l]] -= 1
                l += 1
            result = max(result, i - l + 1)
        return result