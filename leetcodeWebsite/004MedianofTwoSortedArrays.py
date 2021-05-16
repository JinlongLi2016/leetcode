# find kth biggst nums
from typing import List

def topk(nums1, i, nums2, j, k):
	s1, s2 = len(nums1), len(nums2)
	if i >= len(nums1):
		return nums2[j+k-1]
	elif j >= len(nums2):
		return nums1[i+k-1]
	elif k == 1:
		return min(nums1[i], nums2[j])

	delta = k // 2
	p1 = min(len(nums1) - 1, i + delta - 1)
	p2 = min(len(nums2) - 1, j + delta - 1)
	if nums1[p1] < nums2[p2]:
		return topk(nums1, p1+1, nums2, j, k - (p1-i+1))
	else:
		return topk(nums1, i, nums2, p2+1,  k - (p2-j+1))

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    	s1, s2 = len(nums1), len(nums2)
    	total_size = s1 + s2
    	if total_size & 1:
    		return topk(nums1, 0, nums2, 0, (total_size+1) // 2)
    	else:
    		return (topk(nums1, 0, nums2, 0, total_size//2) +
    			topk(nums1, 0, nums2, 0, total_size//2 + 1)) / 2