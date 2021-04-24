# 排序



# 插入排序

# 交换排序

## 冒泡排序

## 快排

对lst进行原地排序

```python
def quicksort(lst):
   qs(lst, 0, len(lst)) # 对[start, end)进行排序
   
def qs(lst, start, end):
   if start >= end:
       return
   mid = split(lst, start, end) # start < end must fit
   qs(lst, start, mid)
   qs(lst, mid+1, end)

def split(A, start, end):
   pivot = A[start]
   i, j = start, start + 1
   while j < end:
       if A[j] <= pivot: # 小于等于pivot的元素应该都放在前半部，因为最后会把pivot放在位置i
           i += 1
           if i != j:
               A[i], A[j] = A[j], A[i]
       j += 1 #【don't forget to update me】
   A[start], A[i] = A[i], A[start]
   return i
```

* note:上面 '<' 在排序里面也是ok的！但是存在一部分等于k的元素可能会在最终位置i的后面

# 选择排序



# 归并排序

```python
def MergeSort(A, start, end):# 对A[start:end] 进行归排
   if start + 1 < end:
       mid = (start + end) // 2
       MergeSort(A, start, mid)
       MergeSort(A, mid, end)
       Merge(A, start, mid, end)

def Merge(A, start, mid, end):
   B = A. copy()
   i, j = start, mid
   k = start
   while i < mid and j < end:
       if B[i] < B[j]:
           A[k] = B[i]; k += 1; i += 1
       else:
           A[k] = B[j]; k += 1; j += 1
   while i < mid:
       A[k] = B[i]
       k += 1
       i += 1
   while j < end:
       A[k] = B[j]
       k += 1
       j += 1
```



# 基数排序

# 外部排序



# 总结

时间复杂度、稳定性

外部排序怎么做？数据量太大，无法放入内存中。