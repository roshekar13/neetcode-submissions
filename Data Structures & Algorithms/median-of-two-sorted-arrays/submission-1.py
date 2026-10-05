class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # force num1 to be smaller
        if len(nums1) > len(nums2): nums1,nums2 = nums2,nums1

        len1, len2 = len(nums1), len(nums2)
        L, R = 0, len1
        half = (len1 + len2 + 1) // 2
        while L <= R:
            i = (L+R)//2
            j = half - i
            A_l = nums1[i-1] if i>0 else float('-inf')
            B_l = nums2[j-1] if j>0 else float('-inf')
            A_r = nums1[i] if i<len(nums1) else float('inf')
            B_r = nums2[j] if j<len(nums2) else float('inf')
            if A_l <= B_r and B_l <= A_r:
                if (len1 + len2) % 2 == 1: return float(max(A_l, B_l))
                return float((max(A_l, B_l) + min(A_r, B_r)) / 2.0)
            elif B_l > A_r: L = i + 1  # Take more from nums1
            else: R = i - 1
        return -1.0