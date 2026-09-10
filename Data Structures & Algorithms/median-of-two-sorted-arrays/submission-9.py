class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # valid cut: left1 <= right2 and
        # left2 <= right1 (What...)

        # oh this is just making it convoluted putting it like this. all in all, we just want to split both arrays in half such that the left halves create the merged left half and the right halves created the left merged half

        # 1 3 5 | 14
        # 2 4   | 8 9 11

        # -> 1 2 3 4 5 | 8 9 11 14
        # since this is odd its then the end of the left array, 5

        # take the middle and cut btw. it, defaulting
        # to putting the left on the left side

        # a valid cut gets you exactly
        # - the left parts from both arrays add up to half total
        # - no # in our left array > any # in right array

        # 0. find the smaller of the two arrays
        A, B = nums1, nums2
        total = len(A) + len(B)
        # get the "half" mark so that we can subtract against it to find how much we need from our other array B
        half = total // 2

        # make A the smaller of the two arrays
        if len(A) > len(B):
            A, B = B, A

        # 1. we need to partition such that the left halves
        # create the left half
        left, right = 0, len(A) - 1

        while True:
            mid_a = (left + right) // 2
            mid_b = half - mid_a - 1 - 1

            # calculate the partition values
            # if mid_a is still "in bounds" - use it
            # otherwise, default it to -inf such that we compare it later
            
            if mid_a >= 0:
                a_left_part = A[mid_a]
            else:
                a_left_part = -(float("inf"))
            
            if mid_a + 1 < len(A):
                a_right_part = A[mid_a + 1]
            else:
                a_right_part = (float("inf"))
            
            if mid_b >= 0:
                b_left_part = B[mid_b]
            else:
                b_left_part = -(float("inf"))
            
            if mid_b + 1 < len(B):
                b_right_part = B[mid_b + 1]
            else:
                b_right_part = (float("inf"))

            # if theyre unbalanced
            if a_left_part <= b_right_part and b_left_part <= a_right_part:
                if total % 2 == 1: # odd case
                    return min(a_right_part, b_right_part)
                return (max(a_left_part, b_left_part) + min(a_right_part, b_right_part)) / 2
            
            elif a_left_part > b_right_part:
                right = mid_a - 1
            
            else:
                left = mid_a + 1
            