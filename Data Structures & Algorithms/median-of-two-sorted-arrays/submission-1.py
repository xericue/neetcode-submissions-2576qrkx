class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2 # integer divison

        # run BS on the smaller of the two arrays
        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A) - 1
        while True: # lazy???
            mid_a = (left + right) // 2 # A
            mid_b = half - mid_a - 1 - 1 # INDEX # arrays
            # are indexed at zero... so get the numebr of
            # values

            # if mid_a is still in bounds, use it
            # otherwise, default it to -inf
            if mid_a >= 0:
                A_left_part = A[mid_a]
            else:
                A_left_part = -(float("inf")) # value @ left partition to compare
            
            # gone too far to right - compare to infinity
            if mid_a + 1 < len(A):
                A_right_part = A[mid_a + 1] # value RIGHT after
            else:
                A_right_part = float("inf")
                
            # if mid_b is still in bounds, use it
            # otherwise, default it to -inf
            if mid_b >= 0:
                B_left_part = B[mid_b]
            else:
                B_left_part = -(float("inf")) # value @ left partition to compare
            
            # gone too far to right - compare to infinity
            if mid_b + 1 < len(B):
                B_right_part = B[mid_b + 1] # value RIGHT after
            else:
                A_right_part = float("inf")

            if A_left_part <= B_right_part and B_left_part <= A_right_part:
                # odd
                if total % 2:
                    return min(A_right_part, B_right_part)
                # even
                return (max(A_left_part, B_left_part) + min(A_right_part, B_right_part)) / 2
            
            elif A_left_part > B_right_part:
                right = mid_a - 1
            else:
                left = mid_a + 1