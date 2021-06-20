# 146LRUCache

Design a data structure that follows the constraints of a **[Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU)**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, ***evict*** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

---

* M1

```python
from collections import deque 


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.contains_size = 0
        
        self.priority_queue = deque([])

    def get(self, key: int) -> int:
        if key in self.dict:
            self.priority_queue.remove(key)
            self.priority_queue.appendleft(key)
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.priority_queue.remove(key)
            self.priority_queue.appendleft(key)
        else: # new key
            if self.contains_size == self.capacity:
                del self.dict[self.priority_queue.pop()]
                self.contains_size -= 1
            self.priority_queue.appendleft(key)
            self.dict[key] = value
            
            self.contains_size += 1
```

