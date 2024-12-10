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

## 6 Month (11/11/24) (just include problems not included in 3 month)

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

### longest substring without repeating characters

- id: 3
- how
  - use hash table to save index of key, and check if new incoming char is in hash table
- [here](../README.md#无重复字符的最长子串)

### 3 sum

- id: 15
- how
  - outer loop to fix one, then problem reduced to two sum

### divide intervals into minimum number of groups

- id: 2406
- same as meeting rooms II (253)

### longest common prefix

- id: 14
- [here](../README.md#最长公共前缀)
- how
  - longest possible: shortest str
  - consider first str's char is prefix char, check the rest of strs if they share the same prefix
    - if yes -> continue to check next char
    - if no -> return current prefix

### reverse nodes in k group

- id: 25
- how
  - combination of two problems: reverse linked list and move pointer by k steps

### trapping rain water

- id: 42
- [here](../README.md#接雨水)
- how
  - decompose to three patterns, iterate forward and backward

### sqrt(x)

- id: 69
- how
  - binary search
  - note: end state, where left and right is, and what is the relation between left and the result we want

### climbing stairs

- id: 70
- [here](../README.md#爬楼梯)
- how: dp

### remove duplicates from sorted list

- id: 83

### Binary Tree Level Order Traversal

- id: 102

### gas station

- id: 134
- tag: greedy, simulation
- [here](../README.md#加油站)

### LRU cache

- id: 146
- [here](../README.md#LRU缓存)

### Implement Trie (Prefix Tree)

- id: 208
- [here](../README.md#实现前缀树)

### Delete Node in a Linked List

- id: 237
- [here](../README.md#删除链表中的节点)
- trick to delete current node without knowing previous node

### slide window maximum

- id: 239
- [here](../README.md#滑动窗口最大值)
- how: monotonic queue

### add digits

- id: 258
- how: while loop :)

### Missing Number

- id: 268
- how: set1.difference(set2)

### Nim Game

- id: 292
- how
  - n % 4 != 0 -> I win
  - n % 4 == 0 -> I lose
  - why:
    - first three: I win
    - fourth: I will definitely lose
    - dp update: `dp[i] = (not dp[i-1]) or (not dp[i-2]) or (not dp[i-3])`
    - which means only when all previous three are True, I will lose (repeat in period of 4)
    - therefore, no need to build dp table -> just check remainder

### coin change

- id: 322
- [here](../README.md#零钱兑换)
- how: dp

### decode string

- id: 394
- [here](../README.md#字符串解码)
- how: stack

### kth largest element in a stream

- id: 703
- tag: heap
- how
  - using heap :)

### Preimage Size of Factorial Zeroes Function

- id: 793
- math...

### number of subarrays with bounded maximum

- id: 795
- tag: DP, Sliding Window, MARK
- how
  - `num < left` -> follow left, res += left
  - `num > right` -> no valid subarray
  - in between
    - if no prev: the this is prev
    - if have prev: res += i - prev

### Smallest Range I

- id: 908
- how
  - score = max - min
  - after min score: max - k and min + k, overall: max - min + 2 \* k, but need to limit it non-negative

### Smallest Range II

- id: 910
- tag: Math, MARK
- how
  - core idea: make smaller larger and make larger smaller
  - how to do this:
    - smaller larger (1):`A[i] + K, A[0] + K`
    - larger smaller (2): `A[i + 1] - K, A[-1] - K`
  - when will meet the min difference:
    - when (1) becomes max and (2) becomes min, then it's potentially min difference.

### Reverse Substrings Between Each Pair of Parentheses

- id: 1190
- tag: Stack
- how
  - similar approach to other decoding string with brackets

### Count Ways to Build Rooms in an Ant Colony

- id: 1916
- tag: DFS, MARK
- [ref](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/solutions/1299540/python-c-clean-dfs-solution-with-explanation/?source=vscode)
<!-- todo -->
