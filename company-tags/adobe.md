# Adobe

## 3 Month (11/11/24)

### Minimum Processing Time

- id: 2895
- name: minimum-processing-time
- how
  - sort two array
  - match min `processorTime` with max `task` time

### integer to roman

- id: 12
- done, find from above

### number of islands

- id: 200
- dfs

### median of two sorted arrays

- id: 4
- interesting! D&C! find it [here](../README.md#寻找两个正序数组的中位数)

### container with most water

- id: 11
- greedy! find it at [here](../README.md#盛最多水的容器)

### next permutation

- id: 31
- simulation, find it [here](../README.md#下一个排列)

### group anagrams

- id: 49
- hash table, find it [here](../README.md#字母异位词分组)
- another approach: use the sorted one as key, and append all other anagrams to the array

### meeting rooms II

- id: 253
- tag: two pointers, simulation, MARK
- how
  - decompose start and end
  - reconstruct starts and ends
  - use two pointers to track start and end
    - if `end > start` -> don't need a new room, we can reuse previous rooms `e += 1`
    - if `end < start` -> there's a meeting happening, need another room, `room += 1`
  - `s += 1`
  
### random pick with weight

- id: 528
- tags: random, simulation, MARK
- how
  - [ref](https://leetcode.com/problems/random-pick-with-weight/solutions/154044/java-accumulated-freq-sum-binary-search/?source=vscode)
  - use prefix sum (determine interval of each weight)
    - eg. `[1,2,3,4,5]` -> `[1,3,6,10,15]`; intervals to return index: `[(1,1), (2,3), (4,6), (7,10), (11,15)]`
    - then use binary search to get the index
    
### count pairs of similar strings

- id: 2506
- name: count-pairs-of-similar-strings
- tag: hash table, string
- how
  - use hash table to store unique chars, then count the number of words with same unique chars
  - note: unique chars need to be sorted

### majority element

- id: 169
- [here](../README.md#多数元素)
- voting algo

### reverse linked list

- id: 206
- note: start from `cur=None`, `next_node=head`

### add two numbers

- id: 2
- how
  - add, full sum and carry