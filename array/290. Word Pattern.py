class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strs = str.split(' ')
        if len(pattern) != len(strs):
            return False
        m = {}
        for i, p in enumerate(pattern):
            if p not in m:
                if strs[i] not in m.values():
                    m[p] = strs[i]
                else:
                    return False
            elif m[p] != strs[i]:
                return False
        return True
