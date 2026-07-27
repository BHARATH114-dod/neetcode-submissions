class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        murg = nums1 + nums2
        murg.sort()
        totallen = len(murg)
        if totallen % 2 == 0:
            return (murg[totallen // 2 - 1 ] + murg[totallen // 2]) / 2.0
        else:
            return murg[totallen // 2]