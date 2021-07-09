# 274Hindex

Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `ith` paper, return compute the researcher's `h`**-index**.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): A scientist has an index `h` if `h` of their `n` papers have at least `h` citations each, and the other `n − h` papers have no more than `h` citations each.

If there are several possible values for `h`, the maximum one is taken as the `h`**-index**.

* M1：先排序，再二分搜索。排序的平均时间复杂度为$O(nlgn)$

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(key=lambda x: -x)
        if citations[0] == 0:
            return 0
        i, j = 0, len(citations)
        while i < j:
            mid = (i + j) // 2
            if citations[mid] > mid and (mid==len(citations)-1 or citations[mid+1] <= mid+1):
                return mid + 1
            elif citations[mid] > mid:
                i = mid + 1
            else:
                j = mid - 1
        return i +  1
```

* LC 使用桶排的思想

```java
public int hIndex(int[] citations) {
    int n = citations.length;
    int[] buckets = new int[n+1];
    for(int c : citations) {
        if(c >= n) {
            buckets[n]++;
        } else {
            buckets[c]++;
        }
    }
    int count = 0;
    for(int i = n; i >= 0; i--) {
        count += buckets[i];
        if(count >= i) {
            return i;
        }
    }
    return 0;
}
```

  

时间复杂度On,空间复杂度On