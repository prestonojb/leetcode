class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = dict()
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if dct.get(tuple(count)) is not None:
                dct[tuple(count)].append(s)
            else:
                dct[tuple(count)] = [s]
        
        return dct.values()