class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for words in strs:
            sorted_words = "".join(sorted(words))
        
            if sorted_words not in group:
                group[sorted_words] = []

            group[sorted_words].append(words)
        return list(group.values())