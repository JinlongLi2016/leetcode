# def helper(A, l1, B, l2, k):
#     if (l1 > l2): return helper(B, l2, A, l1, k)
#     if (l1 == 0): return B[k-1]
#     if (k==1): return min(A[0], B[0])

#     ia = min(l1, k//2); ib = (k - ia)
#     if A[ia-1] < B[ib - 1]:
#         return helper(A[ia:], l1 - ia, B, l2, k - ia)
#     elif A[ia - 1] > B[ib - 1]:
#         return helper(A, l1, B[ib:], l2 - ib, k - ib)
#     else:
#         return A[ia-1]


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         l1, l2 = len(nums1), len(nums2)
#         total = l1 + l2
#         if total % 2 != 0:
#             return helper(nums1, l1, nums2, l2, total // 2 + 1)
#         else:
#             return (helper(nums1, l1, nums2, l2, total//2)
#                    + helper(nums1, l1, nums2, l2, total//2 + 1) )/ 2.


def helper(A, l1, B, l2, k): #　
    if (l1 > l2): return helper(B, l2, A, l1, k)
    if (l1 == 0): return B[l2 - k]
    if (k==1 or k == 0): return max(A[l1-1], B[l2-1])

    delta = k // 2
    ia = max(0, l1 - delta); ib = max(0, l2 - delta)
    if A[ia] < B[ib]:
        return helper(A, l1, B, ib, k - l2 + ib)
    elif A[ia] > B[ib]:
        return helper(A, ia, B, l2, k - l1 + ia)
    else:
        if k - l2 + ib - l1 + ia == 0:
            return A[ia]
        return helper(A, ia, B, ib, k - l2 + ib - l1 + ia)


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l1, l2 = len(nums1), len(nums2)
        total = l1 + l2
        if total % 2 != 0:
            return helper(nums1, l1, nums2, l2, total // 2 + 1)
        else:
            return (helper(nums1, l1, nums2, l2, total//2)
                   + helper(nums1, l1, nums2, l2, total//2 + 1) )/ 2.


if __name__ == '__main__':
    s = Solution()
    print(
        s.findMedianSortedArrays([-1, 0, 1], [2, 3, 4, 5]))