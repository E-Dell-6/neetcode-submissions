class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphaStrs = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in alphaStrs:
                alphaStrs[key] = []
            alphaStrs[key].append(s)

        return list(alphaStrs.values())

        
