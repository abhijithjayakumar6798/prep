class Solution(object):
    def groupAnagrams(self, strs):
        seen=defaultdict(list)
        for i in strs:
            key=''.join(sorted(i))
            seen[key].append(i)
        return list(sorted(seen.values()))