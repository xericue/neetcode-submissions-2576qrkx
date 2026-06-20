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

            # if mid_a is still in bounds, use it; otherwise, default it to -inf
            # negative infinity as the left partition to compare in case our
            # middle is too bad
            A_left_part = A[mid_a] if mid_a >= 0 else -(float("inf"))
            A_right_part = A[mid_a + 1] if mid_a + 1 < len(A) else float("inf")
            
            B_left_part = B[mid_b] if mid_b >= 0 else -(float("inf"))
            B_right_part = B[mid_b + 1] if mid_b + 1 < len(B) else float("inf")
            # if its gone too far to the right, float("inf")

            # IF THE RIGHTMOST ELEMENT OF EACH ARRAY'S LEFT PARTITION IS LESS THAN
            # THE OTHER'S RESPECTIVE NEXT ELEMENT, then start calculating the medium
            if A_left_part <= B_right_part and B_left_part <= A_right_part:

                if total % 2 == 1: # odd case
                    return min(A_right_part, B_right_part)

                return (max(A_left_part, B_left_part) + min(A_right_part, B_right_part)) / 2
            
            elif A_left_part > B_right_part:
                right = mid_a - 1
            else:
                left = mid_a + 1