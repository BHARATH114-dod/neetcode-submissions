class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_seq = 0
        for n in nums:
            if n-1 not in numset:
                len = 0
                while n + len in numset:
                    len += 1
                max_seq = max(len, max_seq)
        return max_seq