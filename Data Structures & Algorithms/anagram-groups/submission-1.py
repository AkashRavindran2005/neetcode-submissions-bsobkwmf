class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in d:
                d[key].append(strs[i])
            else:
                d[key].append(strs[i])
        return list(d.values())