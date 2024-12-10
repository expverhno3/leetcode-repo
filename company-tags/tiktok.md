### word search

- id: 79
- name: word-search
- tag: Array, String, Backtracking, Matrix
- how
  - backtracking
  - some details
    - need to check the boundary / if this char is what we want / if this char visited before

### LRU 缓存

- id: 146
- name: lru-cache
- tag: Design, Hash Table, Linked List, Doubly-Linked List, MARK
- how
  - use two dict to indicate "linked list"
    - `before` and `next`: key -> next/before key (next and before refer to if this key is "recently used")
  - `_delete`: reconnect and remove from all dict
  - `_connect`: connect linked list in two dictionary
  - `_append`: add new key to the "end" of linked list (where just before the `tail`)

### 无重复字符的最长子串

- id: 3
- name: longest-substring-without-repeating-characters
- tag: Hash Table, String, Sliding Window
- how
  - special hashtable design: (char, index)
    - why:
      - easy to check if new incoming char in the sliding window
      - easy to know where the left and right is to calculate the length
  

### 合并区间

- id: 56
- name: merge-intervals
- tag: Array, Sorting
- how
  - sort based on left bound
  - compare left bound and right bound to check if interval i can be merged with interval (i-1)

### word break II

- id: 140
- tag: Backtracking, MARK
- how
  - backtracking, keep track of current path
  - trick: use path as args, and when goes to next depth, pass `path + [word]` to avoid complexity of undo choice


### 最长递增子序列

- id: 300
- name: longest-increasing-subsequence
- tag: Array, Binary Search, Dynamic Programming, MARK
- how
  - [ref](https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/?source=vscode), solution 2
  - init idea: once we meet a smaller value, we create a new subsequence, used it as the first element
    - but this idea will cause multiple subsequences to keep track at the same time, which will slow down
  - optimize: if we find a smaller value, we can replace old elements in subsequence with this smaller value (how to find place: bisect)
  - then result is length of this subsequence