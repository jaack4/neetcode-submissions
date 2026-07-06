class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_freqs = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            
            string_freqs[tuple(freq)].append(s)
        
        return list(string_freqs.values())
            
