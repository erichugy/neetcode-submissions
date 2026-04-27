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
        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            B,A = nums1, nums2
        
        na = len(A)
        nb = len(B)
        nt = (na + nb)

        half = nt // 2
        isOdd = nt % 2

        l, r = 0, na - 1

        INF = 1e6 + 1
        NEG_INF = -INF

        # let x = na // 2 and x = half - m

        while True:
            m = (l + r) // 2
            x = half - m - 2



            leftA = A[m] if m >= 0 else NEG_INF
            rightA = A[m + 1] if m + 1 < na else INF
            leftB = B[x] if x >= 0 else NEG_INF
            rightB = B[x + 1] if x + 1 < nb else INF
            print("Start")
            print(f'm: {m}')
            print(leftA)
            print(rightA)
            print(f'x: {x}')
            print(leftB)
            print(rightB)
            print("\n")

            if leftA <= rightB and leftB <= rightA:
                if isOdd:
                    return min(rightA,rightB)
                else:
                    return (min(rightA,rightB) + max(leftA,leftB)) / 2
            elif leftA > rightB: # make A smaller
                r = m - 1
            else: # Make A Bigger
                l = m + 1
            
                



            
        