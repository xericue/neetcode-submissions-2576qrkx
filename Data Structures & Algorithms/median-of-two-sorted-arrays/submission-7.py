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
            # get middle values
            mid_a = (left + right) // 2 # A - smaller array
            mid_b = half - mid_a - 1 - 1 
            # the - 1 - 1 is to fix the fact that arrays are zero-indexed lol
            # but this is just like. if we have total 12 elements, half is 6, then mid_a is 3.
            # mid_b would then be 3, but we have to fix that index wise


            # calculate partition values to find the respective halves
            # if mid_a is still in bounds, use it; otherwise, default it to -inf
            # negative infinity as the left partition to compare in case our
            # middle is too bad
            A_left_part = A[mid_a] if mid_a >= 0 else -(float("inf"))
            A_right_part = A[mid_a + 1] if mid_a + 1 < len(A) else float("inf")
            
            B_left_part = B[mid_b] if mid_b >= 0 else -(float("inf"))
            B_right_part = B[mid_b + 1] if mid_b + 1 < len(B) else float("inf")
            # if its gone too far to the right, float("inf")

            # if your halves are correct, start returning
            # IF THE RIGHTMOST ELEMENT OF EACH ARRAY'S LEFT PARTITION IS LESS THAN
            # THE OTHER'S RESPECTIVE NEXT ELEMENT, then start calculating the medium
            if A_left_part <= B_right_part and B_left_part <= A_right_part:

                if total % 2 == 1: # odd case
                    return min(A_right_part, B_right_part)
                # otherwise, you need to make a calculation of the middle two elements
                # ... which are actually the pivots after the correct "half" mark on
                # each array. so, you need to get the correct max and min of each
                # e.g. if you have 3 and 4 of your middle you actually wanna pick 3 and 4,
                # not 6 and 7 if your arrays go [2, 3, 7] and [1, 4, 6, 9] or something.
                return (max(A_left_part, B_left_part) + min(A_right_part, B_right_part)) / 2
            
            # otherwise cases (imperfect halving), fix your halves
            # 1. the rightmost element of A's left partition > the first element past B's half
            # -> we have to move right down so that the middle point is lesser, giving us less
            # elements in A's partition so that B can hold more
            # it's sort of a dynamic challenge where we constantly have to pick out the halving 
            elif A_left_part > B_right_part:
                right = mid_a - 1

            # 2. rightmost element of A's left partition <= first element past B's half
            # -> we have to move mid up so that we can fix our halving well
            else:
                left = mid_a + 1