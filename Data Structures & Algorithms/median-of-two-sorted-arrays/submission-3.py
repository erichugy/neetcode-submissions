class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        """
        Solution
        - First arbitrarily take half from each array
            - do this using l,r; m = (l + r) // 2
        - check if these two partitions correctly form the bottom half of all numbers
            do so by checking if the next number in nums1 to the right of the partition 
            is larger than the last number in the bottom partition of nums2. Then do it vice versa.
            If this is not true, then we need to find the next resize the arrays. 
            
            if nums1's partition is too big for example, then move
            the left pointer of the nums2 to median + 1

            then that means that if we take y numbers from nums2, we need to take 
            half - y = x numbers from nums1
        """
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1