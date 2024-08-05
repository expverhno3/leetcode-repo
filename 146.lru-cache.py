#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from collections import deque


class LRUCache:

    # --- implementation from https://leetcode.com/problems/lru-cache/solutions/45926/python-dict-double-linkedlist/comments/185966
    def __init__(self, capacity):
        self.size = capacity
        self.cache = {}
        self.next, self.before = {}, {}  # basic double linked list
        self.head, self.tail = "^", "$"
        self._connect(self.head, self.tail)

    def _connect(self, prev, after):
        self.next[prev] = after
        self.before[after] = prev

    def _delete(self, key):
        """delete one key"""
        self._connect(self.before[key], self.next[key])
        del self.before[key], self.next[key], self.cache[key]

    def _append(self, key, val):
        self.cache[key] = val
        # reconnect: the key at tail to `key`, and `key` to tail
        self._connect(self.before[self.tail], key)
        self._connect(key, self.tail)
        if len(self.cache) > self.size:  # over capacity
            self._delete(self.next[self.head])  # delete the LRU
    
    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key] # get value
        self._delete(key) # delete
        self._append(key, val) # append to make it "new", indicating recently used
        return val
    
    def put(self,key,value):
        if key in self.cache:
            self._delete(key)
        self._append(key, value)
        

    # --- my implementation
    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.data_table = {}
    #     self.keys = deque([])
    #     self.is_full = False

    # def get(self, key: int) -> int:
    #     if key in self.data_table:
    #         self.keys.append(key)
    #         return self.data_table[key]
    #     else:
    #         return -1

    # def put(self, key: int, value: int) -> None:
    #     if key in self.data_table:
    #         self.data_table[key] = value
    #         self.keys.append(key)
    #     else:
    #         if self.is_full:
    #             tmp = self.keys.popleft()
    #             while tmp in self.keys:
    #                 tmp = self.keys.popleft()
    #             del self.data_table[tmp]
    #         else:
    #             self.is_full = False if self.capacity > len(self.data_table.keys()) + 1 else True
    #         self.data_table[key] = value
    #         self.keys.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
