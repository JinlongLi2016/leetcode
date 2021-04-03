class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        j = i + nums[i]
        k = 0
        maxIdx = 0
        while j < len(nums) and i <　j:
            for t in range(i, j+1):
                if t < len(nums):
                    if t + nums[t] > k:
                        maxIdx = t
                        k = t + nums[t]
                i = k
                j = k + nums[k]
                k = j
        return j >= len(nums)



class Solution:
    # 1）只有一个元素 2）n=1
    # 有没有其他异常情况？防御性编程
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        i = 1

        while i < n:
            p = p.next
            i += 1

        q = head
        while p.next is not None:
            p = p.next
            q = q.next

        if p == q:
            p = head
            if p == q:
                return None
            else:
                while p.next != q:
                    p = p.next
                p.next = None
                return head
        else:
            q.val = q.next.val
            q.next = q.next.next
        return head